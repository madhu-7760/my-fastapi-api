import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_create_and_list_users():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/users/", json={"name": "Bob"})
        assert r.status_code == 201
        body = r.json()
        assert body["name"] == "Bob"

        r2 = await ac.get("/users/")
        assert r2.status_code == 200
        assert any(u["name"] == "Bob" for u in r2.json())
