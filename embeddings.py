from openai import OpenAI

from langchain.embeddings.base import Embeddings

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

# def get_embedding(text, model="text-embedding-3-small"):
#     text = text.replace("\n", " ")
#     return client.embeddings.create(input = [text], model=model).data[0].embedding


def get_embedding(text, model="text-embedding-3-small"):
    # from openai import OpenAI
    # import os
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

class CustomEmbedding(Embeddings):
    def embed_documents(self, texts):
        return [get_embedding(text) for text in texts]

    def embed_query(self, text):
        return get_embedding(text)