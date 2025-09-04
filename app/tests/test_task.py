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
async def test_task_crud_flow(client):
    username = "bit_crud"
    password = "secure123"

    # Registro y login
    await client.post(
        "/auth/register", json={"username": username, "password": password}
    )
    res = await client.post(
        "/auth/login", json={"username": username, "password": password}
    )
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear tarea
    task_data = {"title": "CRUD Task", "description": "Initial description"}
    res = await client.post("/tasks/", json=task_data, headers=headers)
    assert res.status_code == 201
    task = res.json()
    task_id = task["id"]
    assert task["title"] == "CRUD Task"

    # Obtener tarea específica
    res = await client.get(f"/tasks/{task_id}", headers=headers)
    assert res.status_code == 200
    assert res.json()["id"] == task_id

    # Actualizar tarea
    updated_data = {"title": "Updated Task", "description": "Updated description"}
    res = await client.put(f"/tasks/{task_id}", json=updated_data, headers=headers)
    assert res.status_code == 200
    updated_task = res.json()
    assert updated_task["title"] == "Updated Task"

    # Eliminar tarea
    res = await client.delete(f"/tasks/{task_id}", headers=headers)
    assert res.status_code == 204

    # Verificar que ya no existe
    res = await client.get(f"/tasks/{task_id}", headers=headers)
    assert res.status_code == 404
