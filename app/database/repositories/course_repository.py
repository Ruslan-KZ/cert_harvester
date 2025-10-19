from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.model.models import Course
from app.schemas.course.create import CourseCreate

async def add_course(db: AsyncSession, course: CourseCreate):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

async def get_courses(db: AsyncSession):
    result = await db.execute(select(Course))
    return result.scalars().all()
