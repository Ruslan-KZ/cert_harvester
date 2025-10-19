from pydantic import BaseModel
from typing import Optional



class CourseCreate(BaseModel):
    user_id: int
    link: str
    name: Optional[str]
    duration_hours: Optional[float]