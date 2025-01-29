from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserType(str, Enum):  
  ADMIN = "ADMIN"
  CUSTOMER = "CUSTOMER"

class CreateUserRequest(BaseModel):
  first_name: str
  last_name: str
  email: EmailStr
  phone: str
  password: str
  type: UserType = UserType.CUSTOMER

class UpdateUserRequest(BaseModel):
  id: Optional[str] = None
  first_name: Optional[str] = None
  last_name: Optional[str] = None
  email: Optional[EmailStr] = None
  phone: Optional[str] = None
  password: Optional[str] = None
  type: Optional[UserType] = None

class Token(BaseModel):
  access_token: str
  refresh_token: str
  token_type: str


class GoogleUser(BaseModel):
  sub: str
  email: EmailStr
  first_name: str
  last_name: str

class RefreshTokenRequest(BaseModel):
  refresh_token: str

class LoginRequest(BaseModel):
  email: str
  password: str