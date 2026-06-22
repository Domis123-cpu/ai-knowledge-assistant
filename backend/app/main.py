from fastapi import FastAPI
from app.api.v1.routes_chat import router as chat_router
from app.api.v1.routes_documents import router as documents_router
from app.api.v1.routes_health import router as health_router

app = FastAPI(title="AI Knowledge Assistant – Modern RAG")

# Podpinamy routery
app.include_router(health_router)
app.include_router(documents_router)
app.include_router(chat_router)
