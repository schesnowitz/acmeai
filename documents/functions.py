from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate
from langchain.indexes import VectorstoreIndexCreator
from documents.models import Session

# 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

import os


def document_llm_qa(file_url, query, document, user):
    os.environ["OPENAI_API_KEY"] = user.profile.open_api_key
    llm = OpenAI(temperature=0.1, verbose=True, openai_api_key="OPENAI_API_KEY")

    pdf = ".pdf"
    if pdf in file_url:
        # print(f"file_url PDF {file_url[1:]}")
        loader = PyPDFLoader(file_url[1:])
        documents = loader.load_and_split()

    else:
        loader = TextLoader(file_url[1:])
        documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_documents(texts, embeddings)

    prompt_template = """Use the following context to answer the question. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        chain_type_kwargs=chain_type_kwargs,
    )
    response = qa.run(query)

    save_document_session(document, user, query, response)


def pdf_llm(file_url, query):
    llm = OpenAI(temperature=0.1, verbose=True)

    loader = PyPDFLoader(file_url)
    documents = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    docsearch = FAISS.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="map_reduce", retriever=docsearch.as_retriever()
    )

    response = qa.run(query)


def save_document_session(document, user, query, response):
    ds = Session(created_by=user, document=document, input=query, response=response)
    ds.save()
