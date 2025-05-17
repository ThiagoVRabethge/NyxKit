from sqlmodel import Session, select

from config.database import engine
from models.items import Items


def handle_get_items_by_id(id: int):
    with Session(engine) as session:
        item = session.exec(select(Items).where(Items.id == id)).first()

        return item
