from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from bson import ObjectId

class UserType(str, Enum):  
  ADMIN = "ADMIN"
  CUSTOMER = "CUSTOMER"

class User(BaseModel):
  id: Optional[str] = Field(None, alias="_id")
  first_name: str
  last_name: str
  email: str
  phone: Optional[str] = None
  password: Optional[str] = None
  type: UserType
  google_sub: Optional[str] = None

  class Config:
    populate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}

  def to_dict(self, exclude_id: bool = True):
    data = self.model_dump(by_alias=True)
    if exclude_id:
      data.pop("_id", None) 
    return data