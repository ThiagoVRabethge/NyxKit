from fastapi import APIRouter, Depends
from items.get_items import handle_get_items
from security.verify_jwt_token import handle_verify_jwt_token
from items.get_items_by_id import handle_get_items_by_id

routes = APIRouter(
  dependencies=[Depends(handle_verify_jwt_token)]
)

@routes.get("/items")
def get_items():
  return handle_get_items()

@routes.get("/items/{id}")
def get_items_by_id(id: int):
  return handle_get_items_by_id(id)
