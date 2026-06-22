# backend/app/api/v1/routes_chat.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.rag.chat_chain import rag_answer
from app.db.session import SessionLocal
from app.db.models import Conversation

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    session_id: str
    query: str


class ChatResponse(BaseModel):
    answer: str
    rewritten_query: str
    num_context_docs: int
    sources: list[str]
    conversation_id: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ChatResponse)
async def chat(req: ChatRequest, db=Depends(get_db)):
    rag_result = rag_answer(req.query)

    conv = Conversation(
        session_id=req.session_id,
        user_message=req.query,
        assistant_message=rag_result["answer"],
    )
    db.add(conv)
    db.commit()
    db.refresh(conv)

    return ChatResponse(
        answer=rag_result["answer"],
        rewritten_query=rag_result["rewritten_query"],
        num_context_docs=rag_result["num_context_docs"],
        sources=rag_result["sources"],
        conversation_id=conv.id,
    )
