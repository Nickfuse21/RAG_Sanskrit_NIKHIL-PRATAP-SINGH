import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""       

import chromadb
from dotenv import load_dotenv
from google import genai                      

load_dotenv()

CHROMA_PATH = "chroma_db"                    
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(
    name="sanskrit"                                               
)

user_query = input("Write your query in Sanskrit:\n\n")  

results = collection.query(                         
    query_texts=[user_query],
    n_results=12
)

print("Docs Found:", results["documents"])

docs_text = "\n\n".join(
    [doc for sub in results["documents"] for doc in sub]
)

system_prompt = f"""
Answer ONLY using the provided Sanskrit text.
Infer from nearest relevant context.
If impossible, say: I don't know.

--------------------
Provided Text:
{docs_text}
"""

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(      
    model="gemini-2.5-flash",
    contents=[system_prompt, user_query]
)

print("\n\n---------------------\n\n")
print(response.text)
