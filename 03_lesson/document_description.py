# Opisywanie metadanymi załadowanych dokumentów

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

chat = ChatOpenAI()

loader = TextLoader('documents.md')
documents = loader.load()
document = documents[0]

# print(document)

# Dzielimy bardzo długi string na podstawie napotkanego znaku podwójnego entera
fragments = document.page_content.split('\n\n');

for fragment in fragments:
    print(fragment)
    print('\n')

# Deklarujemy pustą tablicę, którą będziemy uzupełniać dokumentami tworzonymi w pętli
docs = []
# Wykonujemy pewną instrukcję na każdym elemencie tablicy fragments
for fragment in fragments:
    # Tworzymy nowy obiekt doc na podstawie klasy Document
    doc = Document(page_content=fragment, metadata={"source": ""})
    # Stworzony obiekt doc przekazujemy do ówcześnie zadeklarowanej tablicy docs
    docs.append(doc)

print(docs)

doc_descriptions = []

for doc in docs:
    # Podczas wywoływania metody invoke, przypisujemy jej wynik jako kolejny element listy doc_descriptions. 
    doc_descriptions.append(chat.invoke([
        SystemMessage(content='''
        Your task is to describe the given sentence using one of the following words: Simon, Simba, Honda. Return only the related word. Do not add other content. Additional comments are unnecessary.
        '''),
        HumanMessage(content=f'Sentence: {doc.page_content}')
    ]))


for index, description in enumerate(doc_descriptions):
    docs[index].metadata['source'] = description.content

import json

docs_dict = [doc.to_json() for doc in docs]

with open('documents.json', 'w', encoding='utf-8') as documents:
    json.dump(docs_dict, documents, ensure_ascii=False, indent=4)
