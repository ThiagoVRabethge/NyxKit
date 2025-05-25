from fastapi import APIRouter
from root.docs import handle_read_docs

routes = APIRouter()

@routes.get("/")
def read_docs():
  return handle_read_docs()
