# models/task_model.py
from pydantic import BaseModel, Field
from typing import Optional, List


class Task(BaseModel):
    """
    Representa una tarea completa con id, título y estado.
    Cumple con el esquema 'Task' de OpenAPI.
    """
    id: int = Field(..., example=3)
    title: str = Field(..., example="Repasar examen")
    done: bool = Field(..., example=False)


class TaskCreate(BaseModel):
    """
    Datos para crear una nueva tarea.
    Cumple con el esquema 'TaskCreate' de OpenAPI.
    """
    title: str = Field(..., example="Repasar examen")
    done: Optional[bool] = Field(default=False, example=False)


class TaskUpdate(BaseModel):
    """
    Datos para actualización completa de una tarea.
    Cumple con el esquema 'TaskUpdate' de OpenAPI.
    """
    title: str = Field(..., example="REST básico")
    done: bool = Field(..., example=True)


class TaskPatch(BaseModel):
    """
    Datos para actualización parcial de una tarea.
    Cumple con el esquema 'TaskPatch' de OpenAPI.
    """
    title: Optional[str] = Field(None, example="Nueva tarea parcial")
    done: Optional[bool] = Field(None, example=True)


class ErrorResponse(BaseModel):
    """
    Formato estándar de error.
    Cumple con el esquema 'Error' de OpenAPI.
    """
    error: str = Field(..., example="Not found")


# Almacenamiento en memoria (lista de tareas)
# Este arreglo simula la base de datos en memoria.
tasks_db: List[Task] = [
    Task(id=1, title="Estudiar REST", done=False),
    Task(id=2, title="Hacer práctica", done=True),
]


