from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.api.web.schemas.create import BotRequest
from app.api.web.commands import bot

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/html", response_class=HTMLResponse,tags=["Frontend"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/start_bot",tags=["Frontend"])
async def start_bot_endpoint(data: BotRequest):
    result = bot.start_bot(data.email, data.password, data.links)
    return result
