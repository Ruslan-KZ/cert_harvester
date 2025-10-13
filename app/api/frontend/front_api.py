from fastapi import Depends,APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/html",
            summary= "Html page",
         response_class=HTMLResponse)

async def show_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

