import io
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_upload_docx():
    file = io.BytesIO(b"Test content")
    file.name = "test.docx"

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/documents/upload",
            files={"file": ("test.docx", file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}
        )

    assert response.status_code == 200
