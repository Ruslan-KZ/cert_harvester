from fastapi import APIRouter
from app.api.web import frontend


route = APIRouter()


route.include_router(frontend.router,prefix='/front', tags=["Frontend"])