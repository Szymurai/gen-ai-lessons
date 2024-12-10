from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(find_dotenv())

chat = ChatOpenAI(
    model='gpt-4o-mini',
    callbacks=[StreamingStdOutCallbackHandler()]
)

messages = [
    SystemMessage(content="Hi! How are you?"),
    HumanMessage(content="I'm go")
]

from langchain_core.prompts import ChatPromptTemplate

system_message = "Translate the following into {language}."

user_message = "Text to translate: {text}"

prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("user", user_message)
])

# response = chat.invoke(messages)

# print(response.content)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt | chat | parser

for chunk in chain.stream({
    'language': 'italian',
    'text': 'Cześć! Mam na imię Szymon.'
}):
    print(chunk, end='|', flush=True)
