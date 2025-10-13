# from model.models import User
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select

# async def get_users(db:AsyncSession):
#     stmt = await db.execute(select(User))
#     results = stmt.scalars().all()
#     if not results:
#         return []
#     return [dict(id=u.id, coursera_email=u.coursera_email) for u in results]