from config.database import create_db_and_tables


def handle_on_startup():
    create_db_and_tables()
