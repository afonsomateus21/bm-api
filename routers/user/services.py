from fastapi import Depends, HTTPException
from datetime import timedelta, datetime, UTC
from typing import Annotated
from starlette.config import Config
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from authlib.integrations.starlette_client import OAuth
from jose import jwt, JWTError
from datetime import timedelta, datetime, UTC
from .validators import GoogleUser, UserType
from .models import User
from config.database import users_collection

ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

config = Config(".env")

GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID") or None
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET") or None
SECRET_KEY = config("SECRET_KEY") or None

if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
  raise Exception('Missing env variables')

config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}

starlette_config = Config(environ=config_data)

oauth = OAuth(starlette_config)

oauth.register(
  name='google',
  server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
  client_kwargs={'scope': 'openid email profile'},
)

def authenticate_user(email: str, password: str):
  user: User = users_collection.find_one({ "email": email })

  if not user:
    return False

  if not bcrypt_context.verify(password, user["password"]):
    return False
  return user

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
  encode = {"sub": email, "id": str(user_id)}

  expires = datetime.now(UTC) + expires_delta

  encode.update({"exp": expires})

  return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(email: str, user_id: int, expires_delta: timedelta):
  return create_access_token(email, user_id, expires_delta)


def decode_token(token):
  return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth_bearer)]):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    email: str = payload.get("sub")
    user_id: int = payload.get("id")

    user: User = users_collection.find_one({ "email": email })

    if user is None or user_id is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return user
  except JWTError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")


def token_expired(token: Annotated[str, Depends(oauth_bearer)]):
  try:
    payload = decode_token(token)
    if not datetime.fromtimestamp(payload.get('exp'), UTC) > datetime.now(UTC):
      return True
    return False

  except JWTError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")


def get_user_by_google_sub(google_sub: int):
  return users_collection.find_one({ "google_sub": google_sub })

def check_if_user_already_exits(email: str):
  user = users_collection.find_one({ "email": email })
  return user is not None

def create_user_from_google_info(google_user: GoogleUser):
  print("google_user: ",google_user)
  google_sub = google_user.sub
  email = google_user.email

  existing_user: User = users_collection.find_one({ "email": email })

  if existing_user:
    existing_user["google_sub"] = google_sub
    return existing_user
  else:
    new_user = User(
      first_name=google_user.first_name,
      last_name=google_user.last_name,
      email=google_user.email,
      google_sub=google_sub,
      type=UserType.CUSTOMER
    )
    users_collection.insert_one(new_user.to_dict())
    return new_user

def individual_serial(user) -> dict:
  return {
    "id": str(user["_id"]),
    "first_name": str(user["first_name"]),
    "last_name": str(user["last_name"]),
    "email": str(user["email"]),
    "phone": str(user["phone"]) if user["phone"] is not None else None,
    "type": str(user["type"]),
    "photo": str(user["photo"]) if user["photo"] is not None else None,
    "category": str(user["category"]) if user.get("category") is not None else None,
    "google_sub": str(user["google_sub"]) if user["google_sub"] is not None else None,
    "active": bool(user["active"])  if user["active"] is not None else None,
  }

def list_serial(users) -> list:
  return [individual_serial(user) for user in users]

user_dependency = Annotated[dict, Depends(get_current_user)]