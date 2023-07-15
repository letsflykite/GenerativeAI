from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
import openai

directory = 'pages/'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
print(len(documents))

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))



embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="Your API key")

pinecone.init(
    api_key="Your key",
    environment="env"
)

index_name = "lang-chain-cpcs"
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)







    

