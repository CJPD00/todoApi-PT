# 📝 todoApi-PT

Una API RESTful para gestión de tareas construida con **FastAPI**, **PostgreSQL**, **SQLAlchemy async**, **Alembic** y autenticación JWT. Ideal como base para proyectos personales, educativos o sistemas más complejos.

---

## 🚀 Características

- Registro y login de usuarios con JWT
- CRUD completo de tareas
- Autenticación y autorización por token
- Migraciones con Alembic
- Pruebas automatizadas con `pytest` y `httpx`
- Modularización por servicios y routers
- Compatible con `uv` y `pip`

---

## 🧱 Tecnologías

- **FastAPI**  
- **PostgreSQL**  
- **SQLAlchemy (async)**  
- **Alembic**  
- **Pydantic v2**  
- **pytest + httpx**  
- **uv (gestión de entorno virtual)**

---

## ⚙️ Instalación

### Opción 1: usando `uv` (recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/CJPD00/todoApi-PT.git
cd todoApi-PT

# Crear entorno virtual
uv venv

# Instalar dependencias
uv pip install -r requirements.txt

```

### Opción 2: usando `pip`

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 💾 Base de datos

- Asegúrate de tener PostgreSQL corriendo y accesible.

- Luego Aplica Migraciones
```bash
uv run python -m alembic upgrade head
```


---

## 🚀 Ejecutar la API

```bash
uv run python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📚 Documentación

Puedes encontrar la documentación completa en [Swagger](http://localhost:8000/docs)
localhost:puerto/docs

---

## Variables de entorno
  - `POSTGRES_USER: str`
  - `POSTGRES_PASSWORD: str`
  - `POSTGRES_DB: str`
  - `POSTGRES_HOST: str = "db"`
  - `POSTGRES_PORT: int = 5432`
  - `JWT_SECRET: str`
  - `JWT_ALGORITHM: str = "HS256"`
  - `ACCESS_TOKEN_EXPIRE_MINUTES: int = 30`