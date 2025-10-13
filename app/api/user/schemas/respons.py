from pydantic import BaseModel


class UserRespons(BaseModel):
    id:int
    coursera_email:str
    coursera_password_encrypted:str



    class Config:
        from_attributes = True
