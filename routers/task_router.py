# routers/task_router.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from models.task_model import Task, TaskCreate, TaskUpdate, TaskPatch, ErrorResponse
import services.task_service as service

router = APIRouter()


@router.get("/health", tags=["Health"], response_model=dict)
def get_health():
    """
    Endpoint de salud: devuelve estado, uptime y timestamp.
    """
    import time, datetime
    uptime = time.time() - start_time
    return {
        "status": "ok",
        "uptime": uptime,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }


# Guardamos el tiempo de inicio del servidor
import time
start_time = time.time()


@router.get("/tasks", tags=["Tasks"], response_model=List[Task])
def list_tasks():
    return service.list_tasks()


@router.post("/tasks", tags=["Tasks"], response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    return service.create_task(task_data)


@router.get("/tasks/{id}", tags=["Tasks"], response_model=Task, responses={404: {"model": ErrorResponse}})
def get_task(id: int):
    task = service.get_task(id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Not found"})
    return task


@router.put("/tasks/{id}", tags=["Tasks"], response_model=Task, responses={404: {"model": ErrorResponse}})
def update_task(id: int, task_data: TaskUpdate):
    task = service.update_task(id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Not found"})
    return task


@router.patch("/tasks/{id}", tags=["Tasks"], response_model=Task, responses={404: {"model": ErrorResponse}})
def patch_task(id: int, task_data: TaskPatch):
    task = service.patch_task(id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Not found"})
    return task


@router.delete("/tasks/{id}", tags=["Tasks"], status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": ErrorResponse}})
def delete_task(id: int):
    deleted = service.delete_task(id)
    if not deleted:
        raise HTTPException(status_code=404, detail={"error": "Not found"})
    return None

