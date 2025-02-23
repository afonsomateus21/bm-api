from fastapi import APIRouter, Request, HTTPException, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.requests import Request
from starlette import status
from .models import User
from .services import bcrypt_context, individual_serial, create_user_from_google_info, authenticate_user, get_user_by_google_sub, create_access_token, list_serial, user_dependency, create_refresh_token, token_expired, decode_token, check_if_user_already_exits
from .validators import CreateUserRequest, UpdateUserRequest, Token, RefreshTokenRequest, LoginRequest, UserType, GoogleUser, FileUploadRequest
from config.database import users_collection
from datetime import timedelta
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from supabase import create_client, Client

config = Config(".env")

GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = config("GOOGLE_REDIRECT_URI")
SUPABASE_SERVICE_ROLE_KEY = config("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_PROJECT_URL = config("SUPABASE_PROJECT_URL")

auth_router = APIRouter(prefix="/auth", tags=["User"])

oauth = OAuth(config)
oauth.register(
  name="google",
  client_id=GOOGLE_CLIENT_ID,
  client_secret=GOOGLE_CLIENT_SECRET,
  access_token_url="https://oauth2.googleapis.com/token",
  authorize_url="https://accounts.google.com/o/oauth2/auth",
  api_base_url="https://www.googleapis.com/oauth2/v1/",
  server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
  client_kwargs={"scope": "openid email profile"},
)

supabase: Client = create_client(SUPABASE_PROJECT_URL, SUPABASE_SERVICE_ROLE_KEY)

@auth_router.get("/google/login")
async def login_google(request: Request):
  return await oauth.google.authorize_redirect(request, GOOGLE_REDIRECT_URI)

@auth_router.get("/google/callback")
async def auth_google(request: Request):
  try:
    user_response = await oauth.google.authorize_access_token(request)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        
  user_info = user_response.get("userinfo")

  print(user_info)

  google_user = GoogleUser(
    sub=user_info.get("sub"),
    email=user_info.get("email"),
    first_name=user_info.get("given_name"),
    last_name=user_info.get("family_name")
  )

  existing_user = get_user_by_google_sub(google_user.sub)

  if existing_user:
    print("Existing user")
    user = existing_user
  else:
    print("Creating user")
    user = create_user_from_google_info(google_user)
    print("user created: ", user)

  access_token = create_access_token(user.email, user.id, timedelta(days=7))
  refresh_token = create_refresh_token(user.email, user.id, timedelta(days=14))

  return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"} 
  
@auth_router.post("/user/customer", status_code=status.HTTP_201_CREATED)
async def create_customer(create_user_request: CreateUserRequest):
  create_user_model = User(
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    password=bcrypt_context.hash(create_user_request.password),
    type=UserType.CUSTOMER,
    phone=create_user_request.phone,
    photo=create_user_request.photo,
    email=create_user_request.email
  )

  if (check_if_user_already_exits(create_user_model.email)):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists.")

  result = users_collection.insert_one(create_user_model.to_dict())

  user_created = users_collection.find_one({ "_id": result.inserted_id })

  return individual_serial(user_created)

@auth_router.post("/user/admin", status_code=status.HTTP_201_CREATED)
async def create_admin(create_user_request: CreateUserRequest, current_user: user_dependency):
  if str(current_user["type"]) != "ADMIN":
    raise HTTPException(status_code=403, detail="You are not authorized to create this admin.")
  
  create_user_model = User(
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    password=bcrypt_context.hash(create_user_request.password),
    type=UserType.ADMIN,
    phone=create_user_request.phone,
    photo=create_user_request.photo,
    email=create_user_request.email,
    category=create_user_request.category,
    active=True
  )

  if (check_if_user_already_exits(create_user_model.email)):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists.")

  result = users_collection.insert_one(create_user_model.to_dict())

  user_created = users_collection.find_one({ "_id": result.inserted_id })

  return individual_serial(user_created)

@auth_router.get("/user/admin/{id}", status_code=status.HTTP_200_OK)
async def get_admin(id: str, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  user = users_collection.find_one({ "_id": ObjectId(id), "type": UserType.ADMIN })

  if user is None:
    raise HTTPException(status_code=404, detail="User not found.")
  
  user["_id"] = str(user["_id"])
  if "password" in user:
    del user["password"]
  
  return jsonable_encoder(user)

@auth_router.get("/user/admin", status_code=status.HTTP_200_OK)
async def list_admin(current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  users = list_serial(users_collection.find({ "type": UserType.ADMIN }))
  
  return users

@auth_router.get("/user/me", status_code=status.HTTP_200_OK)
async def read_me(current_user: user_dependency):
  print(current_user)
  return individual_serial(current_user)

@auth_router.post("/user/upload-photo")
async def upload_photo(request: FileUploadRequest):
  try:
    file_path = f"users/{request.file_name}"

    response = supabase.storage.from_("users").create_signed_upload_url(file_path)

    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"]["message"])

    return {"url": response["signedUrl"], "file_path": file_path}

  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not upload the image.")

@auth_router.put("/user/{id}", status_code=status.HTTP_200_OK)
async def edit_user(id: str, update_user_request: UpdateUserRequest, current_user: user_dependency):
  if (str(current_user["type"]) != "ADMIN") and (str(current_user["_id"]) != str(id)):
    raise HTTPException(status_code=403, detail="You are not authorized to update this user.")

  update_data = update_user_request.model_dump(exclude_unset=True)
  result = users_collection.update_one(
    {"_id": ObjectId(current_user["_id"])}, 
    {"$set": dict(update_data)}
  )

  if result.modified_count == 0:
    raise HTTPException(status_code=400, detail="No changes were made to the user.")
  
  updated_user = users_collection.find_one({"_id": ObjectId(current_user["_id"])})

  updated_user["_id"] = str(updated_user["_id"])
  if "password" in updated_user:
    del updated_user["password"]

  return jsonable_encoder(updated_user)

@auth_router.delete("/user/{id}", status_code=status.HTTP_200_OK)
async def remove_user(id: str, current_user: user_dependency):
  if (str(current_user["type"]) != "ADMIN") and (str(current_user["_id"]) != str(id)):
    raise HTTPException(status_code=403, detail="You are not authorized to remove this user.")
  
  result = users_collection.delete_one({ "_id": ObjectId(current_user["_id"]) })

  if result.deleted_count == 0:
    raise HTTPException(status_code=404, detail="User not found.")
  
  return { "success": True, "message": "User successfully removed." }

@auth_router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(request: LoginRequest):
  user = authenticate_user(request.email, request.password)

  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

  access_token = create_access_token(user["email"], user["_id"], timedelta(days=7))
  refresh_token = create_refresh_token(user["email"], user["_id"], timedelta(days=14))

  return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@auth_router.post("/refresh", response_model=Token)
async def refresh_access_token(refresh_token_request: RefreshTokenRequest):
  token = refresh_token_request.refresh_token

  if token_expired(token):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token is expired.")

  user = decode_token(token)

  access_token = create_access_token(user["name"], user["_id"], user["email"], timedelta(days=7))
  refresh_token = create_refresh_token(user["name"], user["_id"], user["email"], timedelta(days=14))

  return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

