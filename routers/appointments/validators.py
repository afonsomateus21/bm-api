from pydantic import BaseModel
import datetime
from typing import Optional

class CreateAppointmentRequest(BaseModel):
  professional_id: str
  customer_id: str
  service_id: str
  date: str
  hour: int
  is_notifiable: bool

class UpdateAppointmentRequest(BaseModel):
  id: Optional[str] = None
  service_id: Optional[str] = None
  date: Optional[str] = None 
  hour: Optional[int] = None
  is_notifiable: Optional[bool] = None