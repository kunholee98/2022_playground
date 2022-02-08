from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    description: str = None
    email: EmailStr

class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str