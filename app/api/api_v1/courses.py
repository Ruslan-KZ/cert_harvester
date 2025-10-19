from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.course.create import CourseCreate
from app.schemas.course.respons import CourseResponse

from app.database.db import get_db
from app.database.repositories.course_repository import add_course, get_courses
from typing import List


router = APIRouter()

@router.post("/",
             summary="Добавляем курсы в БД",
              response_model=CourseResponse)

async def api_add_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    return await add_course(db, course)

@router.get("/",
            summary="Получаем все курсы",
             response_model=List[CourseResponse])

async def api_get_courses(db: AsyncSession = Depends(get_db)):
    return await get_courses(db)
