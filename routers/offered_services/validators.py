from pydantic import BaseModel, field_validator
from .models import ServiceCategory
from typing import Optional

class CreateOfferedServiceRequest(BaseModel):
  title: str
  description: str
  category: ServiceCategory
  professional_id: str
  duration: int
  price: float

  @field_validator("duration")
  def validate_duration(cls, value):
    if value <= 0:
      raise ValueError("Duration must be greater than 0.")
    return value

  @field_validator("price")
  def validate_price(cls, value):
    if value < 0:
      raise ValueError("Price must not be negative.")
    return value
  
class UpdateOfferedServiceRequest(BaseModel):
  id: Optional[str] = None
  title: Optional[str] = None
  description: Optional[str] = None
  category: Optional[ServiceCategory] = None
  professional_id: Optional[str] = None
  duration: Optional[int] = None
  price: Optional[float] = None

  @field_validator("duration")
  def validate_duration(cls, value):
    if value <= 0:
      raise ValueError("Duration must be greater than 0.")
    return value

  @field_validator("price")
  def validate_price(cls, value):
    if value < 0:
      raise ValueError("Price must not be negative.")
    return value