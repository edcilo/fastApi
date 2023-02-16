from datetime import datetime
from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field

from .commonSchema import PaginationMetadataSchema, PaginationParamsSchema


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(UserBaseSchema):
    pass


class UserSchema(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserPaginationSchema(BaseModel):
    data: List[UserSchema]
    pagination: PaginationMetadataSchema


class PaginationOrderColumnParam(str, Enum):
    id = "id"
    name = "name"
    email = "email"
    created_at = "created_at"


class UserPaginationParamsSchema(PaginationParamsSchema):
    order_column: PaginationOrderColumnParam = Field(default="created_at")
