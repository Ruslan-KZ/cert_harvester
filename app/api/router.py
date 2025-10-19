from fastapi import APIRouter
from app.api.frontend.views import router as frontend_router
from app.api.api_v1.users import router as user_router
from app.api.api_v1.courses import router as course_router

route = APIRouter()


route.include_router(frontend_router,prefix="/frontend",tags=["FRONTEND"])
route.include_router(user_router,prefix="/user_v1",tags=["USER"])
route.include_router(course_router,prefix="/course_v1",tags=["COURSE"])