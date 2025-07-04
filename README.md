# Quantum-Computing Lecture **RAG** Assistant

An end-to-end Retrieval-Augmented Generation (RAG) chatbot that answers questions about the lecture notes in **`data/qc_lecture_md.md`**.  
It uses **LangChain**, **FAISS**, and **OpenAI GPT** models.

---

## 📋 Quick-start checklist

| # | Step | Command / File |
|---|------|----------------|
| 1 | **Add your OpenAI key** | Create `.env` in the project root and add:<br>`OPENAI_API_KEY=sk-********************************` |
| 2 | **Install dependencies** | `pip install -r requirements.txt` |
| 3 | **Generate the vector DB** | `python generate_embeddings.py` |
| 4 | **Chat in the terminal** | `python main.py` |


---

## 🔍 What each step does

1. **`.env`** – stores the environment variable `OPENAI_API_KEY`.  
   All scripts load it automatically with **python-dotenv**.


2. **Requirements** – installs  
   `langchain`, `langchain-community`, `langchain-openai`, `faiss-cpu`, `openai`, `tiktoken`, `python-dotenv`.

3. **`generate_embeddings.py`**  
   * Reads `data/qc_lecture_md.md`  
   * Splits the text into 1000-character chunks (300 overlap)  
   * Calls OpenAI embeddings through `CustomEmbedding`  
   * Stores vectors in a **FAISS** index at `vector_db/qc_lecture_db/`

4. **`main.py`** – CLI chatbot  
   * Loads the FAISS index and embeds user queries  
   * Retrieves top-k chunks and feeds them to GPT-4o (or GPT-3.5) via LangChain’s **ConversationalRetrievalChain**.




