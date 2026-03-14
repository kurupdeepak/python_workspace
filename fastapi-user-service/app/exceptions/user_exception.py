from fastapi import status

from app.exceptions.app_exceptions import AppException


class UserNotFoundException(AppException):

    def __init__(self,id):
        super().__init__(
            message=f"User not found {id}",
            status_code=status.HTTP_404_NOT_FOUND,
            error="USER_NOT_FOUND"
        )