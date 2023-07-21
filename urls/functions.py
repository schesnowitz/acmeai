from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import WebBaseLoader, YoutubeLoader, WikipediaLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate
from langchain.indexes import VectorstoreIndexCreator
from urls.models import Urlsession
import os


def url_llm_qa(url_path, query, url_model, user):
    os.environ["OPENAI_API_KEY"] = user.profile.open_api_key
    llm = OpenAI(temperature=0.1, verbose=True, openai_api_key="OPENAI_API_KEY")
    you_tube = "youtube"
    if you_tube in url_path:
        loader = YoutubeLoader.from_youtube_url(url_path, add_video_info=True)
    else:
        ("not youtube")
        loader = WebBaseLoader(web_path=url_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    texts = text_splitter.split_documents(data)

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

    save_url_session(url_model, user, query, response)


def save_url_session(url_model, user, query, response):
    urls = Urlsession(user_id=user, url_id=url_model, input=query, response=response)
    urls.save()
