from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserType(str, Enum):  
  ADMIN = "ADMIN"
  CUSTOMER = "CUSTOMER"

class CategoryType(str, Enum):  
  HAIR = "HAIR",
  FOOT_HAND = "FOOT_HAND",
  LASHES = "LASHES",
  NAILS = "NAILS",
  EYEBROW = "EYEBROW",

class CreateUserRequest(BaseModel):
  first_name: str
  last_name: str
  email: EmailStr
  phone: str
  password: str
  photo: Optional[str] = None
  type: UserType = UserType.CUSTOMER
  category: Optional[CategoryType] = None
  active: bool

class UpdateUserRequest(BaseModel):
  id: Optional[str] = None
  first_name: Optional[str] = None
  last_name: Optional[str] = None
  email: Optional[EmailStr] = None
  phone: Optional[str] = None
  password: Optional[str] = None
  photo: Optional[str] = None
  type: Optional[UserType] = None
  category: Optional[CategoryType] = None
  active: bool = None

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

class FileUploadRequest(BaseModel):
  file_name: str
  mime_type: str