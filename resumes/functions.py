from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import LLMChain

from .models import  PdfContent

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import os

def resume_cover_llm(job_description, resume_url, trigger_text, user, cover_letter):
    os.environ["OPENAI_API_KEY"] = user.profile.open_api_key
    llm = OpenAI(temperature=0.1, verbose=True,openai_api_key="OPENAI_API_KEY" )



    resume_loader = PyPDFLoader(resume_url)
    documents = resume_loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
 
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)

    retriever = db.as_retriever()

    template='''
    I am a job applicant. You are a cover letter writer.
    use my resume information found in the context {context} to create a cover letter.
    use the information in {job_description} to explain why the
    applicant would be a good candidate for the position
    do not make up information, get the applicants information from the resume.
    '''
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{trigger_text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=llm, prompt=chat_prompt, verbose=False)
    raw_response = chain.run({'trigger_text': trigger_text, 
                              'context': texts, 
                              'job_description' : job_description}
                              )


    
    response = raw_response.replace('System:', '').strip() 

    print(f"save_pdf_text###########  {user.id} CL:{cover_letter}")
    save_pdf_text(response, user, cover_letter)
    
# job_description, resume_url, trigger_text, user, cover_letter
def save_pdf_text(llm_text, user, cover_letter):
    
    pdf_text = PdfContent(llm_text=llm_text, user=user, cover_letter=cover_letter)

    pdf_text.save()

