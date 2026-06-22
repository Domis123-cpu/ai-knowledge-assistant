# AI Knowledge Assistant (RAG)

## Opis projektu

Asystent wiedzy oparty o RAG:
- upload PDF/DOCX
- wektorowe wyszukiwanie
- odpowiedzi przez LLM
- historia rozmów
- FastAPI backend
- PostgreSQL
- Docker

## Architektura

- **Frontend:** React (chat UI, upload plików)
- **Backend:** FastAPI (API, logika RAG)
- **DB:** PostgreSQL (historia rozmów, metadane dokumentów)
- **Vector Store:** Chroma (embeddingi dokumentów)
- **LLM:** OpenAI (ChatGPT) lub lokalny model
- **Infra:** Docker + docker-compose
- **CI/CD:** GitHub Actions (testy backendu i frontendu)



## Stack technologiczny

- Python, FastAPI, LangChain
- PostgreSQL, SQLAlchemy, Alembic
- React / TypeScript
- Docker, docker-compose
- GitHub Actions

## Screenshoty

- `docs/screenshots/chat.png`
- `docs/screenshots/upload.png`

## Jak uruchomić

### Wymagania

- Docker + docker-compose
- Klucz OpenAI (opcjonalnie)

### Kroki

```bash
git clone https://github.com/twojanazwa/ai-knowledge-assistant.git
cd ai-knowledge-assistant

# ustaw zmienne środowiskowe
echo "OPENAI_API_KEY=twój_klucz" > .env

docker-compose up --build
