import os
import openai
from fastapi import FastAPI

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/ask")
def ask(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )

    return {
        "question": query,
        "answer": response["choices"][0]["message"]["content"]
    }
