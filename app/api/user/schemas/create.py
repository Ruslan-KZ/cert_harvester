from pydantic import BaseModel, EmailStr,Field
from typing import List


class BotRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)
    links: List[str]
