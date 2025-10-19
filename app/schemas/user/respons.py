from pydantic import BaseModel
from typing import List
from app.schemas.course.respons import CourseResponse



class UserResponse(BaseModel):
    id: int
    coursera_email: str
    coursera_password_encrypted: str
    courses: List[CourseResponse] = []

    model_config = {"from_attributes": True}

# class UserResponse(BaseModel):
#     id:int
#     coursera_email:str
#     coursera_password_encrypted:str
    



#     class Config:
#         from_attributes = True
