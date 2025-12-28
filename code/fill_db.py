import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""   

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils import embedding_functions

DATA_PATH = r"data"                   
CHROMA_PATH = r"chroma_db"

emb = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/distiluse-base-multilingual-cased-v2",
    device="cpu"
)

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(
    name="sanskrit",
    embedding_function=emb
)

loader = PyPDFDirectoryLoader(DATA_PATH)        
raw_documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(            
    chunk_size=600,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(raw_documents)

documents = []
metadata = []
ids = []

for i, chunk in enumerate(chunks):
    documents.append(chunk.page_content)
    ids.append("ID" + str(i))
    metadata.append(chunk.metadata)

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids
)

print("DATABASE READY ON CPU!")
