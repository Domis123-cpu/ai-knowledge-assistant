AI Knowledge Assistant — RAG + FastAPI

Inteligentny asystent wiedzy oparty o RAG (Retrieval-Augmented Generation), FastAPI, ChromaDB, LangChain i OpenAI.

Projekt umożliwia:



upload dokumentów (PDF, DOCX)



automatyczne dzielenie na fragmenty



generowanie embeddingów



zapis do wektorowej bazy danych



zadawanie pytań z kontekstem



odpowiedzi generowane przez model LLM



🚀 Technologie

Python 3.10+



FastAPI



LangChain 0.3+



ChromaDB



OpenAI GPT‑4o-mini



Pydantic Settings



Uvicorn



📦 Struktura projektu

Kod

ai-knowledge-assistant/

│

├── backend/

│   ├── app/

│   │   ├── api/

│   │   │   └── v1/

│   │   │       ├── routes\_chat.py

│   │   │       ├── routes\_documents.py

│   │   │       └── routes\_health.py

│   │   ├── rag/

│   │   │   ├── chat\_chain.py

│   │   │   ├── document\_loader.py

│   │   │   ├── embeddings.py

│   │   │   └── vector\_store.py

│   │   ├── core/

│   │   │   └── config.py

│   │   └── main.py

│   ├── data/

│   │   └── chroma/   ← automatycznie generowane

│   ├── .env.example

│   └── requirements.txt

│

└── README.md

🔧 Instalacja i uruchomienie

1\. Sklonuj repozytorium

Kod

git clone https://github.com/Domis123-cpu/ai-knowledge-assistant.git

cd ai-knowledge-assistant/backend

2\. Utwórz plik .env

Kod

cp .env.example .env

Wklej swój klucz OpenAI:



Kod

OPENAI\_API\_KEY=your\_key\_here

3\. Zainstaluj zależności

Kod

pip install -r requirements.txt

4\. Uruchom backend

Kod

uvicorn app.main:app --reload

5\. Otwórz dokumentację API

http://127.0.0.1:8000/docs (127.0.0.1 in Bing)



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

Przykład:



json

{

&#x20; "session\_id": "test1",

&#x20; "query": "O czym jest dokument?"

}

Zwraca:



odpowiedź



przepisane zapytanie



liczbę dokumentów kontekstowych



źródła



Autor

Projekt przygotowany przez Małgorzatę

Repo: https://github.com/Domis123-cpu/ai-knowledge-assistant

