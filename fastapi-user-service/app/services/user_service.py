from typing import Annotated

from fastapi import HTTPException, status, Depends

from app.db.session import get_db
from app.models.user import UserModel
from app.schemas.user_request import UserRequest
from app.schemas.user import User
from sqlalchemy.orm import Session

DBSession = Annotated[Session, Depends(get_db)]


class UserService:
    def create_user(self, user: UserRequest, db: DBSession):
        db_user = UserModel(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_users(self,db: DBSession):
        return db.query(UserModel).all()

    def get_user(self, user_id: int, db: DBSession):
        user = db.get(UserModel, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    def update_user(self, user_id: int, user: UserRequest, db: DBSession):
        db_user = db.get(UserModel, user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        db_user.name = user.name
        db_user.email = user.email
        db.refresh(db_user)
        db.commit()
        return db_user

    def delete_user(self, user_id: int, db: DBSession):
        db_user = db.get(UserModel, user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        db.delete(db_user)
        db.commit()
        return {"message": f"User deleted {user_id}"}


def get_user_service():
    return UserService()
