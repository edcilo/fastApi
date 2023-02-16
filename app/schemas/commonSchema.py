from enum import Enum
from typing import Union

from pydantic import BaseModel, Field


class PaginationOrderParam(str, Enum):
    asc = "asc"
    desc = "desc"


class PaginationMetadataSchema(BaseModel):
    page: int
    per_page: int
    total: int
    prev: Union[int, None]
    next: Union[int, None]


class PaginationParamsSchema(BaseModel):
    order_column: str = Field(default="created_at")
    order: PaginationOrderParam = Field(default="desc")
    page: int = Field(default=1, gt=0)
    per_page: int = Field(default=15, gt=0, le=100)
