from sqlmodel import Session, select

from config.database import engine
from models.items import Items


def handle_delete_items(id: int):
    with Session(engine) as session:
        db_item = session.exec(select(Items).where(Items.id == id)).first()

        session.delete(db_item)

        session.commit()

        return {"success": True}
