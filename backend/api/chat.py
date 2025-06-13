import sys
import os
from fastapi import APIRouter, Request
from pydantic import BaseModel

# Add the backend folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.rag_chain import query_rag

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/")
async def chat(message: Message):
    answer = query_rag(message.message)
    return {"response": answer}
