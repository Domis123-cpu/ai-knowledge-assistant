from pathlib import Path
from typing import Optional, List

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

from app.rag.embeddings import get_embeddings

PERSIST_DIR = Path("data/chroma")


def get_vector_store(persist_directory: Optional[str] = None) -> Chroma:
    persist_dir = Path(persist_directory) if persist_directory else PERSIST_DIR
    persist_dir.mkdir(parents=True, exist_ok=True)

    embeddings = get_embeddings()
    return Chroma(
        collection_name="knowledge_base",
        embedding_function=embeddings,
        persist_directory=str(persist_dir),
    )


def index_documents(docs: List[Document]) -> int:
    vs = get_vector_store()
    vs.add_documents(docs)
    vs.persist()
    return len(docs)
