from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rag_engine import ERPRagEngine
import os
from dotenv import load_dotenv

# Load environment variables (OpenAI API Key)
load_dotenv()

app = FastAPI(title="ERP RAG Assistant API", description="Query ERP data using Natural Language")
rag_engine = ERPRagEngine()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"status": "Healthy", "message": "ERP RAG Assistant is running."}

@app.post("/ask")
def ask_erp(request: QueryRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API Key not configured on server.")
    
    try:
        answer = rag_engine.ask(request.question)
        return {"question": request.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
