from app.db.database import engine, Base
from app.models.user import UserModel

Base.metadata.create_all(bind=engine)