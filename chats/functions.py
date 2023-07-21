from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import LLMChain

from chats.models import Chat

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import os

def chat_llm(prompt, data_file_url, query, instruction_id, user):
    os.environ["OPENAI_API_KEY"] = user.profile.open_api_key
    llm = OpenAI(temperature=0.1, verbose=True,openai_api_key="OPENAI_API_KEY" )
    loader = TextLoader(data_file_url[1:])
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
 
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)

    retriever = db.as_retriever()

    template="You are a helpful assistant. use {context} to answer the users questions. use {prompt_text} do get instructions from the human."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=llm, prompt=chat_prompt)
    raw_response = chain.run({'text': query, 'context': documents, 'prompt_text' : prompt})



    response = raw_response.replace('System:', '').strip() 

    save_chats(instruction_id, user, query, response)


def save_chats(instruction_id, user, query, response):
    chat = Chat(user_id=user, instruction_id=instruction_id, input=query, response=response)
    chat.save()

