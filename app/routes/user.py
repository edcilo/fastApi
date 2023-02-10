from fastapi import APIRouter, Depends, Request
from ..schemas import UserCreateSchema
from ..repositories import UserRepository
from ..models import db


router = APIRouter(
    prefix="/api/v1/users",
)


@router.post("/")
def create_user_route(
    user: UserCreateSchema,
    userRepo = Depends(UserRepository)
):
    db_user = userRepo.create(user.dict())
    return {
        "id": db_user.id,
        "name": db_user.email,
        "version": db_user.password,
    }
