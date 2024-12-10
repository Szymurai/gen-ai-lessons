# Budowa prostego systemu Retrieval Augmented Generation (RAG)

# Instalacja zewnętrznych pakietów Python, z których będziemy korzystać pisząc logikę aplikacji.

# pip install langchain
# pip install langchain-openai
# pip install langchain-community
# pip install "unstructured[md]" nltk
# pip install python-dotenv

# Wczytanie do pliku interesujących nas klas, metod bądź całych pakietów.

# Importujemy klasą odpowiedzialną za nawiązanie połączenia z OpenAI API (wrapper LangChain do OpenAI API Python SDK).
from langchain_openai import ChatOpenAI
# Poniższe wyrażenie powinniśmy już kojarzyć z poprzednich AI-boratoriów. Funkcja find_dotenv() umożliwia wyszukanie pliku '.env', który nie koniecznie musi znajdować się w bieżącym katalogu, lecz może być umieszczony w folderze nadrzędnym
from dotenv import load_dotenv, find_dotenv
# Ponieważ będziemy chcieli przekazać wiadomość systemową i użytkownika do zapytania API, importujemy klasę tworzącą wspomniane rodzaje wiadomości
from langchain_core.messages import HumanMessage, SystemMessage
# Importujemy klasę odpowiedzialną za wczytanie zewnętrznych dokumentów w formacie 'markdown'
from langchain_community.document_loaders import UnstructuredMarkdownLoader
# Za pomocą klasy Document będziemy weryfikować, czy zwracany typ danych z wywołania klasy UnstructuredMarkdownLoader jest 'Documentem'
from langchain_core.documents import Document

# Znajdujemy plik o nazwie .env, a następnie ładujemy zwarte w nim zmienne środowiskowe do systemu.

load_dotenv(find_dotenv())

chat = ChatOpenAI()

# Funkcjonalność wczytania pamięci przechowywanej w pliku 'note.md'

note_path = 'note.md'
loader = UnstructuredMarkdownLoader(note_path)

documents = loader.load()
# Jeśli zwrócona tablica ma więcej niż 1 element zostanie zwrócony błąd
assert len(documents) == 1
# Jeśli element wewnątrz tablicy nie jest obiektem instancji klasy Document również zostanie zwrócony błąd
assert isinstance(documents[0], Document)
# Pobieramy właściwość 'page_content' z obiektu i ją wyświetlamy
content = documents[0].page_content
print('Content: ' + content)
print('\n')
# Pobieramy właściwość 'metadata' z obiektu i ją wyświetlamy
metadata = documents[0].metadata
print('Metadata: \n',  metadata)

messages = [
    SystemMessage(content='''
    # Role
    Hey! Senior Full-stack Developer here. My nickname is 'Qsystent'. I can answer any question related to web technologies like HTML/CSS/JavaScript, Python, generative AI, and modern frameworks i.e., Flask using the context provided below and nothing else.

    # Rules
    - I do not answer any questions that do not relate to the added context
    - I always answer very concisely
    - I always answer truthfully, as if I were under oath
    - Before I answer, I will take a deep breath and think thoroughly about what is provided in the context

    # Example
    - Who are maiko?
    - Sorry, but I will not answer this question, because my answer is limited to the context given.

    # Context
    {}
'''.format(content)),
    HumanMessage(content='Czym interesuje się Szymon? ')
]

answer = chat.invoke(messages)
print(answer.content)
