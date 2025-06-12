from fastapi import APIRouter, Request
from pydantic import BaseModel
from scripts.rag_chain import query_rag

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/")
async def chat(message: Message):
    answer = query_rag(message.message)
    return {"response": answer}
