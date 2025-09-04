from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_db
from app.schemas.user import UserCreate
from app.services.auth_service import registerPost, LoginPost

router = APIRouter()


@router.post("/register")
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await registerPost(user_in, db)


@router.post("/login")
async def login(user_in: UserCreate, db: AsyncSession = Depends(get_db)):

   return await LoginPost(user_in, db)
