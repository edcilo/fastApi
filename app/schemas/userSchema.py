from typing import List, Union

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
