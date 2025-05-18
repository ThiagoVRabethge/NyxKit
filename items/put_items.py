from sqlmodel import Session, select

from config.database import engine
from models.items import Items


def handle_put_items(id: int, item: Items):
    with Session(engine) as session:
        db_item = session.exec(select(Items).where(Items.id == id)).first()

        db_item.name = item.name if item.name is not None else db_item.name

        db_item.description = (
            item.description if item.description is not None else db_item.description
        )

        session.add(db_item)

        session.commit()

        session.refresh(db_item)

        return {"success": True}
