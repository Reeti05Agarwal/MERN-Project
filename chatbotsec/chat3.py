import os
import datetime
from dotenv import load_dotenv

# Import necessary LangChain modules
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader,
)
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_chroma import Chroma
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, create_structured_chat_agent
from langchain_core.tools import Tool
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables from .env
load_dotenv()

# Pull the prompt template from the hub
prompt_template = hub.pull("hwchase17/structured-chat-agent")

# Model initialization
model = OllamaLLM(model="llama3.2")

########################################################################

# Set up directories for notes and database
current_dir = os.path.dirname(os.path.abspath(__file__))
notes_dir = os.path.join(current_dir, "notes")
db_dir = os.path.join(current_dir, "db")

# Check if the notes folder exists
if not os.path.exists(notes_dir):
    raise FileNotFoundError(f"The folder {notes_dir} does not exist. Please check the path.")
else:
    print(f"Notes Directory: {notes_dir}")

# Load text documents from notes directory
documents = []
for root, _, files in os.walk(notes_dir):
    for notes_file in files:
        if notes_file.endswith(".md"):
            file_path = os.path.join(root, notes_file)
            loader = UnstructuredMarkdownLoader(file_path)
            notes_doc = loader.load()
            for doc in notes_doc:
                doc.metadata = {"source": notes_file}
                documents.append(doc)

# Checking if documents are loaded
print(f"Total documents loaded: {len(documents)}")

########################################################################

# Function to create a vector store
def create_vector_store(docs, embeddings, store_name):
    persistent_dir = os.path.join(db_dir, store_name)
    if not os.path.exists(persistent_dir):
        print(f"\n--- Creating vector store {store_name} ---")
        db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_dir)
        print(f"--- Finished creating vector store {store_name} ---")
    else:
        print(f"Vector store {store_name} already exists. No need to initialize.")

# Function to query the vector store
def query_vector_store(store_name, embeddings, query, search_type, search_kwargs):
    persistent_dir = os.path.join(db_dir, store_name)
    if os.path.exists(persistent_dir):
        print(f"\n--- Querying the Vector Store {store_name} ---")
        db = Chroma(persist_directory=persistent_dir, embedding_function=embeddings)
        retriever = db.as_retriever(search_type=search_type, search_kwargs=search_kwargs)

        # Retrieve relevant documents
        relevant_docs = retriever.invoke(query)

        # Prepare the combined input for the model
        combined_input = (
            "Here are some documents that might help answer the question: "
            + query
            + "\n\nRelevant Documents:\n"
            + "\n\n".join([doc.page_content for doc in relevant_docs])
            + "\n\nPlease provide an answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure'."
        )
        return combined_input
    else:
        print(f"Vector store {store_name} does not exist.")

########################################################################

# Define the embedding function
model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}  
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

#########################################################################

# Recursive splitting of documents
print("\n--- Using Recursive Character-based Splitting ---")
docs_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n"])
docs = docs_splitter.split_documents(documents)

# Create vector store
create_vector_store(docs, embeddings, "chroma_db")

# Create a retriever from the vector store
retriever = Chroma(
    persist_directory=os.path.join(db_dir, "chroma_db"),
    embedding_function=embeddings
).as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.1},
)

#########################################################################

# Define system prompt for contextualizing questions
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)

# Create a prompt template for contextualizing questions
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Define system prompt for answering questions
qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

# Create a prompt template for answering questions
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ] 
)

#########################################################################

# Create the question-answer chain
question_answer_chain = create_stuff_documents_chain(model, qa_prompt)

# Create a history-aware retriever
history_aware_retriever = create_history_aware_retriever(
    llm=model,
    retriever=retriever,
    prompt=qa_prompt
)

# Create a retrieval chain that combines the history-aware retriever and the question-answering chain
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Initialize chat history
chat_history = []

# Chat loop
while True:
    query = input("Maria: ")
    if query.lower() == "exit":
        break

    # Query the vector store
    query_result = query_vector_store(
            "chroma_db",
            embeddings,
            query,
            "similarity_score_threshold",
            {"k": 3, "score_threshold": 0.5},
        )

    # Get the AI's response using the RAG chain
    result = rag_chain.invoke({
        "chat_history": chat_history,
        "input": query_result,
        "context": query_result  # Passing query_result as the context
    })

    # Display the AI's response
    print(f"AI: {result['answer']}")

    # Update the chat history
    chat_history.append(HumanMessage(content=query_result))
    chat_history.append(SystemMessage(content=result["answer"]))