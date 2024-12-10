from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv, find_dotenv

from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(find_dotenv())

chat = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="Hi! How are you?"),
    HumanMessage(content="I'm go")
]

memory = ConversationBufferMemory(k=1)

legacy_chain = LLMChain(
    llm=chat,
    prompt=messages,
    memory=memory
)

# chain = memory | chat

response = legacy_chain.invoke()

print(response)
