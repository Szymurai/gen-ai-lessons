# pip install "langserve[all]"
# pip install fastapi

from fastapi import FastAPI

from dotenv import load_dotenv, find_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

load_dotenv(find_dotenv())

system_message = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_message),
    ('user', '{text}')
])

chat = ChatOpenAI()

parser = StrOutputParser()

chain = prompt_template | chat | parser

app = FastAPI(
    title='LangChain Server',
    version='1.0',
    description="A simple API server using LangChain's Runnable interfaces"
)

add_routes(
    app,
    chain,
    path='/chain'
)

if __name__ == '__main__':
    # pip install uvicorn
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
