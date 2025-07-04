from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS


import os
from dotenv import load_dotenv

# from embeddings import get_embedding
from embeddings import CustomEmbedding


with open("data/qc_lecture_md.md", "r") as file:
    raw_text = file.read()
    
    

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=300 
)


chunks = text_splitter.split_text(raw_text)  

# print(f"Total number of chunks: {len(chunks)}")

# documents = [Document(page_content=chunk) for chunk in chunks]

# embeddings = get_embedding(chunks)

embedding = CustomEmbedding()

documents = [Document(page_content=chunk, metadata={"source": f"chunk_{i}"}) for i, chunk in enumerate(chunks)]

db = FAISS.from_documents(documents, embedding=embedding)  
db.save_local("vector_db/qc_lecture_db")