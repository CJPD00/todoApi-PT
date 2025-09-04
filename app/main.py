from fastapi import FastAPI
from app.api.v1 import auth, tasks

app = FastAPI(title="Todos API", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

# @app.get("/health")
# def health():
#     return {"status": "ok"}

