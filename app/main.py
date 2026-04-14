from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG API Running"}

@app.get("/ask")
def ask(q: str):
    return {"answer": f"You asked: {q}"}
