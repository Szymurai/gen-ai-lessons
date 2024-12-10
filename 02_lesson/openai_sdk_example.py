# inicjalizacja połączenia do modelu za pomocą OpenAI API SKD-Python, wraz z wygenerowaną odpowiedzią.

# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

client = OpenAI()

# Tworzymy nową odpowiedź modelu, która będzie dopełnieniem przekazanej wiadomości.
response = client.chat.completions.create(
    model='chatgpt-4o-latest',
    messages=[
        {'role': 'system','content': "Hi! How are you?"},
        {'role': 'user','content': "I'm go"}
    ]
)

print(response.choices[0].message.content)
