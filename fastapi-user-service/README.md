python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

pip freeze > requirements.txt


docker run --name fastapi-postgres \
-e POSTGRES_USER=fastapi \
-e POSTGRES_PASSWORD=fastapi \
-e POSTGRES_DB=fastapi_db \
-p 5432:5432 \
-d postgres:16


fastapi-user-service> python -m app.db.init_db

Production-Style FastAPI Project Structure
app
│
├── main.py
│
├── api
│   └── v1
│       └── routers
│            └── users.py
│
├── core
│   ├── config.py
│   └── security.py
│
├── db
│   ├── database.py
│   └── session.py
│
├── models
│   └── user.py
│
├── schemas
│   ├── user.py
│   ├── user_create.py
│   └── user_update.py
│
├── repositories
│   ├── base_repository.py
│   └── user_repository.py
│
├── services
│   └── user_service.py
│
└── dependencies
    └── auth.py