from pydantic import BaseModel
from enum import Enum

class ServiceCategory(str, Enum):  
  FOOT_AND_HAND = "FOOT_HAND"
  HAIR = "HAIR"
  EXTENSION = "EXTENSION"

class OfferedService(BaseModel):
  title: str
  description: str
  category: ServiceCategory
  professional_id: str
  duration: int
  price: float