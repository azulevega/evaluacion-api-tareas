# main.py
from fastapi import FastAPI
from routers import task_router

app = FastAPI(
    title="API REST Básica de Tareas",
    version="1.0.0",
    description="API mínima para operaciones CRUD sobre el recurso 'tasks'. Incluye endpoint de salud y almacenamiento en memoria."
)

app.include_router(task_router.router)


