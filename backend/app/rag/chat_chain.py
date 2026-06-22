from typing import Dict, Any

from langchain_openai import ChatOpenAI
from app.core.config import settings
from app.rag.vector_store import get_vector_store


def get_llm(model: str = "gpt-4o-mini", temperature: float = 0.1):
    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=model,
        temperature=temperature,
    )


def rewrite_query(user_query: str) -> str:
    llm = get_llm(model="gpt-4o-mini", temperature=0.0)

    system_prompt = (
        "Rewrite the user's query into a clear, self-contained search query. "
        "Do not answer the question."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    resp = llm.invoke(messages)
    return resp.content.strip()


def get_retriever():
    vs = get_vector_store()
    return vs.as_retriever(search_kwargs={"k": 5})


def generate_answer(user_query: str, docs):
    llm = get_llm(model="gpt-4o-mini", temperature=0.1)

    context_text = "\n\n".join(
        f"[Source: {d.metadata.get('source', 'unknown')}] {d.page_content}"
        for d in docs
    )

    system_prompt = (
        "You are an AI Knowledge Assistant. "
        "Answer ONLY using the provided context. "
        "If the answer is not in the context, say you don't know."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"Question: {user_query}\n\nContext:\n{context_text}",
        },
    ]

    resp = llm.invoke(messages)
    return resp.content.strip()


def rag_answer(user_query: str) -> Dict[str, Any]:
    rewritten = rewrite_query(user_query)
    retriever = get_retriever()
    docs = retriever.get_relevant_documents(rewritten)

    answer = generate_answer(user_query, docs)

    return {
        "answer": answer,
        "rewritten_query": rewritten,
        "num_context_docs": len(docs),
        "sources": [d.metadata.get("source", "unknown") for d in docs],
    }
