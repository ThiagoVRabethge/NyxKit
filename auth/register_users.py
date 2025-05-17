from passlib.context import CryptContext
from sqlmodel import Session

from config.database import engine
from models.users import Users


def handle_register_users(user: Users):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    user.password = pwd_context.hash(user.password)

    with Session(engine) as session:
        session.add(user)

        session.commit()

        session.refresh(user)

        return {"sucess": True}
