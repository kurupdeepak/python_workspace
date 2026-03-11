from fastapi import HTTPException, status

from app.schemas.user_request import UserRequest
from app.schemas.user import User


class UserService:

    def __init__(self):
        self.users = {}
        self.sequence = 1

    def create_user(self, user: UserRequest):
        user.id = self.sequence
        self.sequence += 1
        self.users[user.id] = User(
            id=user.id, name=user.name, email=user.email)
        return user

    def get_users(self):
        return list(self.users.values())

    def get_user(self, user_id: int):
        user = self.users.get(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    def update_user(self, user_id: int, user: UserRequest):
        if user_id not in self.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        updated_user = User(
            id=user_id,
            name=user.name,
            email=user.email
        )

        self.users[user_id] = updated_user
        return updated_user

    def delete_user(self, user_id: int):

        if user_id not in self.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        del self.users[user_id]

        return {"message": "User deleted"}


def get_user_service():
    return UserService()
