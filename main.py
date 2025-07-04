from langchain_community.vectorstores import FAISS
from embeddings import CustomEmbedding

# embedding = CustomEmbedding()

# # Load saved index
# db = FAISS.load_local("vector_db/qc_lecture_db", embedding)

# query = "What are quantum gates?"

# results_with_scores = db.similarity_search_with_score(query, k=3)
# for doc, score in results_with_scores:
#     print(f"Score: {score}\n{doc.page_content}\n")

import os
import dotenv 
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPEN_AI_KEY")
)


embedding = CustomEmbedding()
db = FAISS.load_local("vector_db/qc_lecture_db", embedding,
                      allow_dangerous_deserialization=True)


question = "What are quantum gates?"
docs_with_scores = db.similarity_search_with_score(question, k=5)

print(f"Top {len(docs_with_scores)} results for the question: '{question}'\n")

for i, (doc, score) in enumerate(docs_with_scores):
    # print(f"Result {i + 1} (Score: {score}):\n{doc.page_content}\n")
    print(f"Result {i + 1} (Score: {score})\n")

context = "\n\n".join([doc.page_content for doc, _ in docs_with_scores])


response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system",
         "content": "You are a helpful assistant. Use the provided context."},
        {"role": "user",
         "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]
)

print(response.choices[0].message.content)