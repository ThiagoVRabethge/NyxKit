from fastapi import Depends, FastAPI

from auth.auth_routes import routes as auth_routes
from auth.login_users import handle_login_users
from auth.register_users import handle_register_users
from items.delete_items import handle_delete_items
from items.get_items import handle_get_items
from items.get_items_by_id import handle_get_items_by_id
from items.items_routes import routes as items_routes
from items.patch_items import handle_patch_items
from items.post_items import handle_post_items
from items.put_items import handle_put_items
from models.items import Items
from models.users import Users
from root.docs import handle_read_docs
from root.root_routes import routes as root_routes
from root.startup import handle_on_startup
from security.verify_jwt_token import handle_verify_jwt_token

app = FastAPI()


@app.on_event("startup")
def on_startup():
    handle_on_startup()


# root routes

app.include_router(root_routes)

# auth routes

app.include_router(auth_routes)

# items routes

app.include_router(items_routes)
