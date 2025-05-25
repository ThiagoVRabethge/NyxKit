from fastapi import APIRouter
from models.users import Users
from auth.register_users import handle_register_users
from auth.login_users import handle_login_users

routes = APIRouter()

@routes.post("/auth/register-users")
def register_users(user: Users):
  return handle_register_users(user)

@routes.post("/auth/login-users")
def login_users(user: Users):
  return handle_login_users(user)
