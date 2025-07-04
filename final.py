# main.py
import os
import dotenv
from openai import OpenAI
from langchain_community.vectorstores import FAISS
from embeddings import CustomEmbedding  

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

dotenv.load_dotenv()

# client     = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
embedding  = CustomEmbedding()
db         = FAISS.load_local(
                "vector_db/qc_lecture_db",
                embedding,
                allow_dangerous_deserialization=True)   

retriever = db.as_retriever(search_kwargs={"k": 5})
llm = ChatOpenAI(model_name="gpt-4o-mini",
                 openai_api_key=os.getenv("OPEN_AI_KEY"))
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever)



def answer(question: str, k: int = 5, show_docs: bool = True) -> str:
    docs_with_scores = db.similarity_search_with_score(question, k=k)

    # if show_docs:
    #     print("\n— Top matches —")
    #     for i, (doc, score) in enumerate(docs_with_scores, 1):
    #         print(f"[{i}]  score={score:.4f} | {doc.metadata.get('source')}")

    context = "\n\n".join(doc.page_content for doc, _ in docs_with_scores)

    response = client.chat.completions.create(
        model="gpt-4.1",                  
        messages=[
            {
                "role": "system",
                "content":  "You are a helpful assistant. Use only the provided context to answer the user.",
            },
            {
                "role": "system",
                "content": "Be technical and accurate."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    
    # retriever = db.as_retriever(search_kwargs={"k": 5})
    # llm      = ChatOpenAI(model_name="gpt-4o-mini",
    #                    openai_api_key=os.getenv("OPEN_AI_KEY"))
    # qa_chain  = ConversationalRetrievalChain.from_llm(llm, retriever)
    
    chat_history = []
    print("Ask me anything about the lecture notes!  (type 'exit' to quit)\n")
    while True:
        q = input("> ")
        if q.lower() in {"exit", "quit"}:
            break
        result = qa_chain({"question": q, "chat_history": chat_history})
        print(result["answer"], "\n")
        chat_history.append((q, result["answer"]))
    
    # print("Ask me anything about the lecture notes!  (type 'exit' to quit)\n")
    # while True:
    #     q = input("> ").strip()
    #     if q.lower() in {"exit", "quit"}:
    #         break
    #     if not q:
    #         continue         
    #     print()
    #     print(answer(q))
    #     print()
