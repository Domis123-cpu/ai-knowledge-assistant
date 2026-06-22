# backend/app/rag/document_loader.py
from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document



def save_uploaded_file(upload_dir: str, file) -> str:
    upload_path = Path(upload_dir)
    upload_path.mkdir(parents=True, exist_ok=True)
    dest = upload_path / file.filename
    with dest.open("wb") as f:
        f.write(file.file.read())
    return str(dest)


def load_raw_documents(path: str) -> List[Document]:
    path_obj = Path(path)
    suffix = path_obj.suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(str(path_obj))
    elif suffix == ".docx":
        loader = Docx2txtLoader(str(path_obj))
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    docs = loader.load()
    # Dodajemy podstawowe metadata
    for d in docs:
        d.metadata.setdefault("source", str(path_obj.name))
    return docs


def split_documents(docs: List[Document]) -> List[Document]:
    """
    Nowoczesny chunking:
    - mniejsze chunki
    - overlap
    - lepsza jakość retrievalu
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " "],
    )
    return splitter.split_documents(docs)
