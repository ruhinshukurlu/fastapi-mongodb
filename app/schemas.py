from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId


class UserBaseSchema(BaseModel):
    name:str
    email:str
    photo:str
    role:str = None
    created_at:datetime = None
    update_at:datetime = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password:constr(min_length=8)
    passwordConfirm:str
    verified:bool = False


class LoginUserSchema(BaseModel):
    email:EmailStr
    password:constr(min_length=8)
