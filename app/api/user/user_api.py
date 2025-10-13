from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.user.schemas.respons import UserRespons
from app.api.user.schemas.create import BotRequest
from database.db import get_db
from app.api.user.commands.user_crud import add_users, get_users



router = APIRouter()

@router.post("/add_user" ,
    summary= "Добавляем пользователей в БД",
    response_model=dict
)

async def api_add_user(data:BotRequest, db:AsyncSession = Depends(get_db)):
    return await add_users(data,db)

@router.get("/", 
    summary= "Получить всех пользователей",
    response_model=list[UserRespons]
)

async def api_get_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

