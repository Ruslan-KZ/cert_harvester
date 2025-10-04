from pydantic import BaseModel, EmailStr
from typing import List

class BotRequest(BaseModel):
    email: EmailStr
    password: str
    links: List[str]
