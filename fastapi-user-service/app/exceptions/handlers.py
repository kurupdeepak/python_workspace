from fastapi.responses import JSONResponse
from fastapi import Request

from app.exceptions.app_exceptions import AppException
from fastapi.exceptions import RequestValidationError


def register_exception_handlers(app):

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.error,
                "request":request.body,
                "message": exc.message,
                "status": exc.status_code
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):

        return JSONResponse(
            status_code=400,
            content={
                "error": "VALIDATION_ERROR",
                "message": f"Invalid request payload {request.body}",
                "status": 400
            }
        )