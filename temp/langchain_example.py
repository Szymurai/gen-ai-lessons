# inicjalizacja połączenia do modelu za pomocą LangChain, wraz z wygenerowaną odpowiedzią.

# pip install python-dotenv
# pip install langchain
# pip install langchain-openai

from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv(find_dotenv())

chat = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="Hi! How are you?"),
    HumanMessage(content="I'm go")
]

response = chat.invoke(messages)

print(response.content)

# Przykład użycia "łańcuchów"

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = chat | parser

print(chain.invoke(messages))

# Przykład użycia "Prompt Templates"

from langchain_core.prompts import ChatPromptTemplate

system_message = "Translate the following into {language}."

user_message = "Text to translate: {text}"

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("user", user_message)
])

messages = prompt_template.invoke({
    'language': 'italian',
    'text': 'Cześć! Mam na imię Szymon.'
}).to_messages()

# print(type(messages))

# print(messages)

# Ponownie możemy użyć koncepcji "łańcuchów":

chain = prompt_template | chat | parser

print(chain.invoke({
    'language': 'italian',
    'text': 'Cześć! Mam na imię Szymon.'
}))
