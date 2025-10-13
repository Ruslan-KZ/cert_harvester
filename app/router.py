from fastapi import APIRouter
from app.api.frontend.front_api import router as frontend_router
from app.api.user.user_api import router as user_router


route = APIRouter()


route.include_router(frontend_router,prefix="/frontend",tags=["FRONTEND"])
route.include_router(user_router,prefix="/user",tags=["USER"])