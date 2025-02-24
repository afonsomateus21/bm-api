from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ServiceCategory(str, Enum):  
  FOOT_HAND = "FOOT_HAND"
  HAIR = "HAIR"
  NAILS = "NAILS"
  LASHES: "LASHES"

class OfferedService(BaseModel):
  title: str
  description: str
  category: ServiceCategory
  professional_id: str
  duration: int
  price: float
  photo: Optional[str] = None
  active: Optional[bool]