# Przykład tworzenia prostego dokumentu bezpośrednio wywołując klasę Document

from langchain_core.documents import Document

note = Document(page_content='Szymon lubi jeść krewetki.', metadata={"source": "Szymon"})

print(note)
