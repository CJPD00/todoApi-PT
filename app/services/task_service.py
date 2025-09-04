from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.user import User
from fastapi import HTTPException


async def get_task_by_id(task_id: int, db: AsyncSession, user: User) -> Task:
    task = await db.get(Task, task_id)
    if not task or task.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


async def create_task(data: TaskCreate, db: AsyncSession, user: User) -> Task:
    task = Task(**data.model_dump(), owner_id=user.id)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def update_task(
    task_id: int, data: TaskUpdate, db: AsyncSession, user: User
) -> Task:
    task = await get_task_by_id(task_id, db, user)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(task_id: int, db: AsyncSession, user: User):
    task = await get_task_by_id(task_id, db, user)
    await db.delete(task)
    await db.commit()


async def list_tasks(
    db: AsyncSession, user: User, page: int = 1, items_per_page: int = 10
) -> Sequence[Task]:
    skip = (page - 1) * items_per_page
    limit = items_per_page
    result = await db.execute(
        select(Task).where(Task.owner_id == user.id).offset(skip).limit(limit)
    )
    return result.scalars().all()
