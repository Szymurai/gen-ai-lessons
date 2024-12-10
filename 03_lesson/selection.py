# Kod odpowiedzialny za selekcję dokumentu w zależności od pytania zadanego przez użytkownika

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

q = 'Co jest największym priorytetem Simby?'

chat = ChatOpenAI()

notes = [
    {'name': "Szymon (Szymurai)", 'source': "szymon.md"},
    {'name': "Simba (Psimba - Król Pies)", 'source': "simba.md"},
    {'name': "Honda", 'source': "honda.md"}
]

system_message = SystemMessage(content=f'''
# Rules
From among the given notes, select the one corresponding to the user's query and return the path to the file. Do not add unnecessary comments.
                               
# Notes
{', '.join(note['name'] for note in notes)}
File paths: {', '.join(note['source'] for note in notes)}

User query: {q}

Note file path:
''')

file_path = chat.invoke([system_message])

print(file_path.content)
