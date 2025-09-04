from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.services.task_service import (
    create_task,
    get_task_by_id,
    update_task,
    delete_task,
    list_tasks,
)

router = APIRouter()


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create(
    data: TaskCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return await create_task(data, db, user)


@router.get("/", response_model=list[TaskOut])
async def list_all(
    db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)
):
    return await list_tasks(db, user)


@router.get("/{task_id}", response_model=TaskOut)
async def get(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return await get_task_by_id(task_id, db, user)


@router.put("/{task_id}", response_model=TaskOut)
async def update(
    task_id: int,
    data: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return await update_task(task_id, data, db, user)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
     await delete_task(task_id, db, user)
