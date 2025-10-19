from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.model.models import User,Course
from app.model.models import CourseStatusEnum
from app.schemas.user.create import UserCreate


async def add_users(data: UserCreate,db:AsyncSession):
    stmt = await db.execute(select(User).where(User.coursera_email==data.email))
    existing = stmt.scalar_one_or_none()
    if existing:
        return {"status":"Пользователь уже существует!"}
    new_user = User(
        coursera_email=data.email,
        coursera_password_encrypted=data.password 
    )
    db.add(new_user)
    await db.flush()  
    for link in data.links:
        course = Course(
            user_id=new_user.id,
            link=link.strip(),
            status=CourseStatusEnum.pending
        )
        db.add(course)

    await db.commit()
    return {"status": "Пользователь и курсы добавлены"}


async def get_users(db:AsyncSession):
    stmt = await db.execute(select(User))
    results = stmt.scalars().all()
    if not results:
        return []
    return [dict(id=u.id, coursera_email=u.coursera_email) for u in results]