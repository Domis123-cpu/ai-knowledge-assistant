# backend/app/rag/embeddings.py
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings


def get_embeddings():
    """
    Nowoczesne embeddingi z langchain-openai.
    Możesz łatwo podmienić na lokalny model.
    """
    return OpenAIEmbeddings(
        api_key=settings.OPENAI_API_KEY,
        model="text-embedding-3-large",
    )
