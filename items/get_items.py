from sqlmodel import Session, select

from config.database import engine
from models.items import Items


def handle_get_items():
    with Session(engine) as session:
        items = session.exec(select(Items)).all()

        return items
