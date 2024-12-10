from langserve import RemoteRunnable

remote_chain = RemoteRunnable('http://localhost:8000/chain/')
# Zwracany jest string
response = remote_chain.invoke({'language': 'german', 'text': 'Hi! How r y?'})

print(response)
