#!/bin/bash

PROJECT_NAME=fastapi-user-service

mkdir -p $PROJECT_NAME/app/{routers,schemas,services,models,db,core}

touch $PROJECT_NAME/app/main.py
touch $PROJECT_NAME/app/routers/users.py
touch $PROJECT_NAME/app/schemas/user_schema.py
touch $PROJECT_NAME/app/services/user_service.py
touch $PROJECT_NAME/app/models/user.py
touch $PROJECT_NAME/app/db/database.py
touch $PROJECT_NAME/app/core/config.py

touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/Dockerfile
touch $PROJECT_NAME/README.md

echo "FastAPI project structure created!"