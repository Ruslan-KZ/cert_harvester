from fastapi import APIRouter

router = APIRouter()

@router.get("/auth_route")
def auth_route():
    return {"message":" Hello"}