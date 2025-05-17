from sqlmodel import Session

from config.database import engine
from models.items import Items


def handle_post_items(item: Items):
    with Session(engine) as session:
        session.add(item)

        session.commit()

        session.refresh(item)

        return {"success": True}
