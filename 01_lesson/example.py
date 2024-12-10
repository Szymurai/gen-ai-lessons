from openai import OpenAI # Musiałem ustawić odpowiednią ścieżkę do interpretera Python bezpośrednio w moim nowo utworzonym wirtualnym środowisku.

# Tworzymy obiekt na podstawie klasy OpenAI
client_openai = OpenAI()

# Tworzymy zmienną, w której będziemy przechowywać odpowiedź od modelu.

model_response = client_openai.chat.completions.create(
    # ChatLM
    model='gpt-4o',
    messages=[
        {
            'role': 'system',
            'content': 'Jesteś Samurajem programowania specjalizujuącym się w nauczaniu podstaw JavaScript i Python'
        },
        {
            'role': 'user',
            'content': "Wytłumacz mi pojęcie krotki w kontekście programowania w języku Python."
        }
    ]
)

model_message = dict(model_response.choices[0].message)
print(model_message['content'])

# Dziękuję!