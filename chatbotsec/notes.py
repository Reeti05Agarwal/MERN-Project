import os
from langchain_community.document_loaders import (
    TextLoader, 
    UnstructuredMarkdownLoader,
    FireCrawlLoader
)

current_dir = os.path.dirname(os.path.abspath(__file__)) #chatbotsec
notes_dir = os.path.join(current_dir, "notes") 
db_dir = os.path.join(current_dir, "db")

print(current_dir)
print(notes_dir)
print(db_dir)

documents = []
for root, dirs, files in os.walk(notes_dir):
    for notes_file in files:
        if notes_file.endswith(".md"):
            file_path = os.path.join(root, notes_file)
            loader = UnstructuredMarkdownLoader(file_path)
            notes_doc = loader.load()
            for doc in notes_doc:
                doc.metadata = {"source": notes_file}
                documents.append(doc)

# Checking if docs are loaded or not
print(f"Total documents loaded: {len(documents)}")

print(documents)