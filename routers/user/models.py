from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserType(str, Enum):  
  ADMIN = "ADMIN"
  CUSTOMER = "CUSTOMER"

class User(BaseModel):
  name: str
  email: str
  phone: Optional[str] = None
  password: Optional[str] = None
  type: UserType
  google_sub: Optional[str] = None