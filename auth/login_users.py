from datetime import datetime, timedelta

from decouple import config
from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from config.database import engine
from models.users import Users


def handle_login_users(user: Users):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    secret = config("SECRET")

    algorithm = config("ALGORITHM")

    with Session(engine) as session:
        db_user = session.exec(select(Users).where(Users.email == user.email)).first()

        if pwd_context.verify(user.password, db_user.password):
            payload = {
                "id": db_user.id,
                "email": db_user.email,
                "exp": datetime.utcnow() + timedelta(minutes=40),
            }

            token = jwt.encode(payload, secret, algorithm)

            return {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email,
                "jwt_token": token,
            }
        else:
            return {"success": False}
