import warnings, os, dotenv


from langchain_core._api import LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)  

from langchain_openai import ChatOpenAI              
from langchain_community.vectorstores import FAISS   
from langchain.chains import ConversationalRetrievalChain
from embeddings import CustomEmbedding               

dotenv.load_dotenv()                                 

embedding = CustomEmbedding()

db = FAISS.load_local(
    "vector_db/qc_lecture_db",
    embedding,
    allow_dangerous_deserialization=True     
)

retriever = db.as_retriever(search_kwargs={"k": 5})


llm = ChatOpenAI(
    model_name="gpt-4o-mini",               
    temperature=0.2,                        
    openai_api_key=os.getenv("OPEN_AI_KEY") 
)

qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever)




def main() -> None:
    chat_history = []
    print("Ask me anything about the lecture notes!  (type 'exit' to quit)\n")
    while True:
        try:
            question = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGood-bye!")
            break

        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        result = qa_chain({"question": question, "chat_history": chat_history})
        answer = result["answer"]
        print("\n" + answer + "\n")

        chat_history.append((question, answer))


if __name__ == "__main__":
    main()