📘 AI Knowledge Assistant — RAG + FastAPI
Inteligentny asystent wiedzy oparty o Retrieval‑Augmented Generation (RAG), FastAPI, LangChain, ChromaDB i OpenAI.

System umożliwia przetwarzanie dokumentów, generowanie embeddingów, zapis do wektorowej bazy danych oraz zadawanie pytań z kontekstem dokumentów.

🚀 Funkcjonalności
📤 Upload dokumentów
Obsługa PDF i DOCX

Automatyczne dzielenie na fragmenty

Generowanie embeddingów

Zapis do ChromaDB

🔍 RAG – wyszukiwanie kontekstowe
Wyszukiwanie najtrafniejszych fragmentów

Retrieval z wektorowej bazy danych

Przekazywanie kontekstu do modelu LLM

💬 Chat z AI
Zadawanie pytań o treść dokumentów

Odpowiedzi generowane przez model OpenAI GPT‑4o‑mini

Zwracanie źródeł i fragmentów kontekstu

🧩 Modularna architektura
Oddzielone warstwy: API, RAG, embeddings, vector store

Łatwe do rozbudowy i integracji

🧠 Technologie
Obszar	Technologia
Backend	FastAPI, Uvicorn
RAG	LangChain 0.3+, ChromaDB
Embeddings	OpenAI text-embedding-3-small
LLM	OpenAI GPT‑4o‑mini
Konfiguracja	Pydantic Settings
Język	Python 3.10+


📦 Struktura projektu
Kod
ai-knowledge-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── routes_chat.py
│   │   │       ├── routes_documents.py
│   │   │       └── routes_health.py
│   │   ├── rag/
│   │   │   ├── chat_chain.py
│   │   │   ├── document_loader.py
│   │   │   ├── embeddings.py
│   │   │   └── vector_store.py
│   │   ├── core/
│   │   │   └── config.py
│   │   └── main.py
│   ├── data/
│   │   └── chroma/        ← automatycznie generowane
│   ├── .env.example
│   └── requirements.txt
│
└── README.md
🔧 Instalacja i uruchomienie
1️⃣ Sklonuj repozytorium
bash
git clone https://github.com/Domis123-cpu/ai-knowledge-assistant.git
cd ai-knowledge-assistant/backend
2️⃣ Utwórz plik .env
bash
cp .env.example .env
Wklej swój klucz OpenAI:

Kod
OPENAI_API_KEY=your_key_here
3️⃣ Zainstaluj zależności
bash
pip install -r requirements.txt
4️⃣ Uruchom backend
bash
uvicorn app.main:app --reload
5️⃣ Otwórz dokumentację API
http://127.0.0.1:8000/docs

📤 Upload dokumentów
Endpoint:

Kod
POST /documents/upload
Obsługiwane formaty:

PDF

DOCX

Po uploadzie dokument jest:

zapisywany

dzielony na fragmenty

embedowany

zapisywany w ChromaDB

💬 Chat RAG
Endpoint:

Kod
POST /chat
Przykład zapytania:

json
{
  "session_id": "test1",
  "query": "O czym jest dokument?"
}
Zwraca:

odpowiedź modelu

przepisane zapytanie

liczbę dokumentów kontekstowych

źródła

🧑‍💻 Autor
Projekt przygotowany przez Małgorzatę  
Repozytorium: https://github.com/Domis123-cpu/ai-knowledge-assistant
