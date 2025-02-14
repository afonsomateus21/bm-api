from fastapi import FastAPI
from routers.user.controllers import auth_router
from routers.offered_services.controllers import offered_services_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
  SessionMiddleware,
  secret_key=os.getenv("SECRET_KEY"), 
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(offered_services_router, prefix="/api")

