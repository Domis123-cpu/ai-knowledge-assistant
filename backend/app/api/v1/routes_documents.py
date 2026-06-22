# backend/app/api/v1/routes_documents.py
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.rag.document_loader import save_uploaded_file, load_raw_documents, split_documents
from app.rag.vector_store import index_documents

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not (file.filename.lower().endswith(".pdf") or file.filename.lower().endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX are supported.")

    path = save_uploaded_file("uploads", file)
    raw_docs = load_raw_documents(path)
    chunks = split_documents(raw_docs)
    count = index_documents(chunks)

    return {
        "status": "indexed",
        "filename": file.filename,
        "chunks_indexed": count,
    }
