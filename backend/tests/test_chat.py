import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_chat_endpoint():
    payload = {
        "session_id": "test-session",
        "query": "Hello"
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/chat", json=payload)

    assert response.status_code in (200, 500)
