from fastapi import APIRouter,Depends
from typing import Annotated

from app.schemas.user_request import UserRequest
from app.schemas.user import User
from app.services.user_service import UserService,get_user_service
from app.db.session import get_db
router = APIRouter(prefix="/users", tags=["Users"])

UserServiceDep = Annotated[UserService,Depends(get_user_service)]


@router.post("/", response_model=User)
def create_user(user: UserRequest, user_service: UserServiceDep):
    return user_service.create_user(user)


@router.get("/",response_model=list[User])
def get_users(user_service: UserServiceDep):
    return user_service.get_users()


@router.get("/{user_id}",response_model=User)
def get_user(user_id: int,user_service: UserServiceDep):
    return user_service.get_user(user_id)


@router.put("/{user_id}",response_model=User)
def update_user(user_id: int, user: UserRequest, user_service: UserServiceDep):
    return user_service.update_user(user_id, user)


@router.delete("/{user_id}",response_model=str)
def delete_user(user_id: int,user_service: UserServiceDep):
    return user_service.delete_user(user_id)