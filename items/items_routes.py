from fastapi import APIRouter, Depends
from items.get_items import handle_get_items
from security.verify_jwt_token import handle_verify_jwt_token
from items.get_items_by_id import handle_get_items_by_id
from models.items import Items
from items.post_items import handle_post_items
from items.put_items import handle_put_items
from items.delete_items import handle_delete_items
from items.patch_items import handle_patch_items

routes = APIRouter(
  dependencies=[Depends(handle_verify_jwt_token)]
)

@routes.get("/items")
def get_items():
  return handle_get_items()

@routes.get("/items/{id}")
def get_items_by_id(id: int):
  return handle_get_items_by_id(id)

@routes.post("/items")
def post_items(item: Items):
  return handle_post_items(item)

@routes.put("/items/{id}")
def put_items(id: int, item: Items):
  return handle_put_items(id, item)

@routes.patch("/items/{id}")
def patch_items(id: int, item: Items):
  return handle_patch_items(id, item)

@routes.delete("/items/{id}")
def delete_items(id: int):
  return handle_delete_items(id)
