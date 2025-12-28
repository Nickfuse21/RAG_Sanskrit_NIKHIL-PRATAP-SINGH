# Sanskrit Retrieval Augmented Generation (RAG) System
# ---------------------------------------------------
# A CPU-based Sanskrit Question Answering System
# Built using Python, ChromaDB, Sentence Transformers and Gemini API
# ---------------------------------------------------


## // PROJECT OBJECTIVE
- Build a working Retrieval-Augmented Generation (RAG) system
- Support Sanskrit text understanding and question answering
- Ensure the system runs completely on CPU (no GPU usage)
- Retrieve text from documents instead of blind AI generation
- Produce grounded, controlled and non-hallucinatory responses


## // SYSTEM OVERVIEW
# The project follows a simple & logical RAG workflow:
1. Sanskrit PDF documents are placed inside the `data/` folder
2. System reads and extracts Sanskrit text
3. Text is split into meaningful overlapping chunks
4. Embeddings are generated using a multilingual sentence-transformer
5. Embeddings stored in ChromaDB (local vector database)
6. User enters Sanskrit query in terminal
7. Relevant Sanskrit chunks are retrieved
8. Gemini model generates answer using ONLY retrieved context
9. If answer not present → System returns "I don’t know"


## // KEY SYSTEM CHARACTERISTICS
- Fully CPU based execution
- Local persistent ChromaDB storage
- Real Sanskrit text support
- No hallucination behavior
- Clean modular pipeline


## // TECHNOLOGIES, FRAMEWORKS & LIBRARIES

# Programming Language
- Python 3.11+

# Vector Database
- ChromaDB
  -> Stores embeddings
  -> Performs similarity search
  -> Persists data locally

# Embedding & Text Processing
- sentence-transformers
  -> Multilingual embedding model
  -> Supports Sanskrit text
  -> Runs on CPU

- Model Used:
  -> sentence-transformers/distiluse-base-multilingual-cased-v2

- langchain-community
  -> Document loading utilities

- langchain-text-splitters
  -> Splits long Sanskrit text into chunks

- pypdf
  -> Extracts text from PDF files

# Environment & Configuration
- python-dotenv
  -> Safely manages GEMINI API Key

# GPU Disable Mechanism
- os.environ["CUDA_VISIBLE_DEVICES"] = ""
  -> Forces CPU only execution

# Large Language Model
- google-genai (Gemini API)
  -> Generates final answers
  -> Strictly uses retrieved Sanskrit context
  -> Replies "I don’t know" if answer not found


## // FOLDER STRUCTURE
project/
 ├── code/
 │    ├── fill_db.py
 │    ├── ask.py
 │    ├── requirements.txt
 │
 ├── data/
 │    ├── Sanskrit PDFs here
 │
 ├── chroma_db/
 │    ├── auto created database
 │
 ├── report/
 │    ├── Technical Report PDF
 │
 ├── README.md


## // INSTALLATION & SETUP

# STEP 1 — Create Virtual Environment
python -m venv venv

# STEP 2 — Activate Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

# STEP 3 — Install Dependencies
pip install -r requirements.txt

# STEP 4 — Add Gemini API Key
Create `.env` file & add:
GEMINI_API_KEY=your_api_key_here


## // EXECUTION

# STEP 1 — Build Database
python fill_db.py

# STEP 2 — Ask Questions
python ask.py

# Enter Sanskrit Query in Terminal
Example:
कथायाः मुख्योपदेशः कः?


## // FAILURE BEHAVIOUR
# If answer not found:
System safely responds:
"I don't know"


## // CPU ONLY CONFIRMATION
- GPU is disabled
- Embeddings run on CPU
- Model explicitly locked to CPU
- System reproducible on normal laptops


## // CONCLUSION
This project demonstrates a complete, stable and explainable Sanskrit RAG System.
It retrieves, understands and answers Sanskrit queries responsibly,
ensuring correctness, reliability and CPU-only execution.
