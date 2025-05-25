from fastapi import Depends, FastAPI
from auth.login_users import handle_login_users
from auth.register_users import handle_register_users
from items.delete_items import handle_delete_items
from items.get_items import handle_get_items
from items.get_items_by_id import handle_get_items_by_id
from items.patch_items import handle_patch_items
from items.post_items import handle_post_items
from items.put_items import handle_put_items
from models.items import Items
from models.users import Users
from root.docs import handle_read_docs
from root.startup import handle_on_startup
from security.verify_jwt_token import handle_verify_jwt_token
from items.items_routes import routes as items_routes
from auth.auth_routes import routes as auth_routes

app = FastAPI()

# root

@app.on_event("startup")
def on_startup():
    handle_on_startup()

@app.get("/")
def read_root():
    return handle_read_docs()

# auth routes

app.include_router(auth_routes)

# items routes

app.include_router(items_routes)

@app.post("/items", dependencies=[Depends(handle_verify_jwt_token)])
def post_items(item: Items):
    return handle_post_items(item)

@app.put("/items/{id}", dependencies=[Depends(handle_verify_jwt_token)])
def put_items(id: int, item: Items):
    return handle_put_items(id, item)

@app.patch("/items/{id}", dependencies=[Depends(handle_verify_jwt_token)])
def patch_items(id: int, item: Items):
    return handle_patch_items(id, item)

@app.delete("/items/{id}", dependencies=[Depends(handle_verify_jwt_token)])
def delete_items(id: int):
    return handle_delete_items(id)
