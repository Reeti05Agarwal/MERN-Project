import os
import datetime
import ollama
import chromadb

from dotenv import load_dotenv

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter, 
    TextSplitter
) 
from langchain_community.document_loaders import (
    TextLoader, 
    UnstructuredMarkdownLoader,
    FireCrawlLoader
)
 
from langchain_core.messages import (
    HumanMessage, 
    SystemMessage,
    AIMessage
)

from langchain_chroma import Chroma
from langchain.memory import ConversationBufferMemory

from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
    create_structured_chat_agent
)
from langchain_core.tools import Tool

 
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings


########################################################################################

# Load environment variables from .env
load_dotenv()

# Pull the prompt template from the hub
prompt = hub.pull("hwchase17/structured-chat-agent")

# model 
model = OllamaLLM(model="qwen2:0.5b")

# Create a structured Chat Agent with Conversation Buffer Memory
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True
)

client = chromadb.Client()
collection = client.create_collection("my_notes")


############################################################################################

# Define a very simple tool function that returns the current time
def get_current_time(*args, **kwargs):

    now = datetime.datetime.now()   
    return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format

# Define the tools that the agent can use
tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time.",
    ) 
]

# create_structured_chat_agent initializes a chat agent designed to interact using a structured prompt and tools
agent = create_structured_chat_agent(
    llm=model, 
    tools=tools, 
    prompt=prompt
)

# Manage the interaction between the user query, the agent, and the tools and chat history
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    memory=memory,  
    handle_parsing_errors=True,   
)
 

#####################################################################################

 
# Crawling through notes directory
current_dir = os.path.dirname(os.path.abspath(__file__)) #C:\Users\Reeti\Desktop\chatbotsec
notes_dir = os.path.join(current_dir, "notes") #C:\Users\Reeti\Desktop\chatbotsec\notes
db_dir = os.path.join(current_dir, "db") #C:\Users\Reeti\Desktop\chatbotsec\db


# checking if the notes folders are there or not
if not os.path.exists(notes_dir):
    raise FileNotFoundError(
        f"The file {file_path} does not exist. Please check the path"
    )
else:
    print(f"Notes Directory: {notes_dir}")


############################################################################

collection.add()
# Loading text and list of notes
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


# Recursive splitting into text chunks
print("\n--- Using Recursive Character-based Splitting ---")
docs_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n"])
docs = docs_splitter.split_documents(documents)


#########################################################################

# Vector Store

persistent_dir = os.path.join(db_dir, "chroma_db")

if not os.path.exists(persistent_dir):
        print(f"\n--- Creating vector store {store_name} ---")
        db = Chroma.from_documents(
            docs, embeddings, persist_directory=persistent_dir
        )
        print(f"--- Finished creating vector store {store_name} ---")
else:
    print(f"\n--- Querying the Vector Store {store_name} ---")

    db = Chroma(
            persist_directory=persistent_dir, embedding_function=embeddings
        )

    retriever = db.as_retriever(
        search_type=search_type,
        search_kwargs=search_kwargs,
    )

 
#########################################################################

# Summarize and classify each chunk
'''
for text_chunk in docs:
    # Summarization
    print("====SUMMARY====")
    summary = model.invoke("Summarize this text: " + text_chunk.page_content)
    print(f"Summary: {summary}")

    # Classification
    print("====CLASSIFICATION====")
    classification = model.invoke("What is the main topic of this text? " + text_chunk.page_content)
    print(f"Classification: {classification}")
'''
#########################################################################

# Contextualize question prompt
# This system prompt helps the AI understand that it should reformulate the question
# based on the chat history to make it a standalone question
contextualize_q_system_prompt = (
    '''
    Given a chat history and the latest user question and webcrawler information, formulate the answer based on that.
    reform the answer and add you own knowledge to formulate the answer
    '''
)

# Create a prompt template for contextualizing questions
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Create a history-aware retriever
# This uses the LLM to help reformulate the question based on chat history
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# Answer question prompt
# This system prompt helps the AI understand that it should provide concise answers
# based on the retrieved context and indicates what to do if the answer is unknown
qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

#########################################################################


# Initial system message to set the context for the chat
initial_message = "You are an AI assistant that can provide helpful answers using available tools.\nIf you are unable to answer, you can use the following tools: Time and Wikipedia."
memory.chat_memory.add_message(SystemMessage(content=initial_message))

# Chat Loop  
while True:
    query = input("Maria: ")
    if query.lower() == "exit":
        break

    # Add the user's message to the conversation memory
    memory.chat_memory.add_message(HumanMessage(content=query_result))

    print("===Query Result====")
    print(query_result)

    # Invoke the agent with the user input and the current chat history
    response = agent_executor.invoke({"input": query_result})
    print("Bot:", response)

    # Add the agent's response to the conversation memory
    memory.chat_memory.add_message(AIMessage(content=response["output"]))


 
