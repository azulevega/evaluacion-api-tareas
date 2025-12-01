# services/task_service.py
from typing import List, Optional
from models.task_model import Task, TaskCreate, TaskUpdate, TaskPatch, tasks_db


def list_tasks() -> List[Task]:
    """
    Devuelve todas las tareas almacenadas en memoria.
    """
    return tasks_db


def get_task(task_id: int) -> Optional[Task]:
    """
    Busca una tarea por su id.
    """
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None


def create_task(task_data: TaskCreate) -> Task:
    """
    Crea una nueva tarea y la agrega al arreglo en memoria.
    """
    new_id = max([t.id for t in tasks_db], default=0) + 1
    new_task = Task(id=new_id, title=task_data.title, done=task_data.done or False)
    tasks_db.append(new_task)
    return new_task


def update_task(task_id: int, task_data: TaskUpdate) -> Optional[Task]:
    """
    Actualiza completamente una tarea existente.
    """
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task = Task(id=task_id, title=task_data.title, done=task_data.done)
            tasks_db[idx] = updated_task
            return updated_task
    return None


def patch_task(task_id: int, task_data: TaskPatch) -> Optional[Task]:
    """
    Actualiza parcialmente una tarea existente.
    """
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task = task.copy(update=task_data.dict(exclude_unset=True))
            tasks_db[idx] = updated_task
            return updated_task
    return None


def delete_task(task_id: int) -> bool:
    """
    Elimina una tarea por id.
    """
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(idx)
            return True
    return False

