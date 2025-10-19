from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user.create import UserCreate
from app.schemas.user.respons import UserResponse
from app.database.db import get_db
from app.database.repositories.user_repository import add_users, get_users




router = APIRouter()

@router.post("/" ,
    summary= "Добавляем пользователей в БД",
    response_model=dict
)

async def api_add_user(data:UserCreate, db:AsyncSession = Depends(get_db)):
    return await add_users(data,db)

@router.get("/", 
    summary= "Получаем всех пользователей",
    response_model=list[UserResponse]
)

async def api_get_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

