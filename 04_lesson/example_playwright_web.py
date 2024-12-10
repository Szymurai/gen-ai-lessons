# Podstawowy przykład iplementacji modułu Web Search z logiką kodu i Generatynwego AI

# import markdown
import re
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PlaywrightURLLoader, url_playwright, WebBaseLoader

load_dotenv(find_dotenv())

# chat = ChatOpenAI()

# evaluator = url_playwright.PlaywrightEvaluator()


# playwright_loader = PlaywrightURLLoader(['https://neurorush.com'], headless=True, remove_selectors=['header', 'footer'])

base_loader = WebBaseLoader('https://ec.europa.eu/eurostat/web/main/publications')


# playwright_docs = playwright_loader.load()

base_docs = base_loader.load()

# print(playwright_docs[0].metadata)

print('\n')

print(base_docs[0].metadata)


for doc in base_docs:
    i = 1
    url_to_placeholder = {}

    def replace_url(match):

        url = match.group(0)

        if url not in url_to_placeholder:

            placeholder = f'${i}'

            url_to_placeholder[url] = placeholder

            doc.metadata[placeholder] = url

            i += 1

        return url_to_placeholder[url]
    
    doc.page_content = re.sub(r'((http|https):\/\/[^\s]+|\.\/[^\s]+)(?=\))', replace_url, doc.page_content)

print(base_docs[0].metadata)
print('\n')