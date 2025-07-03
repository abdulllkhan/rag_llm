from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPEN_AI_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write the basics of quantum computing in 5 lines"}
  ]
)

print(completion.choices[0].message);