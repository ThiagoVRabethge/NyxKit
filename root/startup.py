from config.database import create_db_and_tables
from migrations.watchmen.watch import watch
from models.items import Items
from models.users import Users

def handle_on_startup():
    watch([Items, Users])
    
    create_db_and_tables()
