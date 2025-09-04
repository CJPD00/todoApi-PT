import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_register_and_login(client):
    username = "bit_test"
    password = "secure123"

    # Registro
    res = await client.post(
        "/auth/register", json={"username": username, "password": password}
    )
    assert res.status_code == 200
    assert res.json()["username"] == username

    # Login
    res = await client.post(
        "/auth/login", json={"username": username, "password": password}
    )
    assert res.status_code == 200
    token = res.json()["access_token"]
    assert token
