from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {"error": "API key missing"}

    return {
        "question": query,
        "answer": "API connected but OpenAI call not added yet"
    }
