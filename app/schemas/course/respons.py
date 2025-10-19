from pydantic import BaseModel
from typing import  Optional
from datetime import datetime
from app.model.models import CourseStatusEnum



class CourseResponse(BaseModel):
    id: int
    link: str
    name: Optional[str]
    duration_hours: Optional[float]
    cert_link: Optional[str]
    status: CourseStatusEnum
    created_at: datetime
    finished_at: Optional[datetime]

    model_config = {"from_attributes": True}