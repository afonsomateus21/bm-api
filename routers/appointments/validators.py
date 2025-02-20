from pydantic import BaseModel
import datetime
from typing import Optional

class CreateAppointmentRequest(BaseModel):
  professional_id: str
  service_id: str
  date: datetime.date
  hour: datetime.time
  is_notifiable: bool

class UpdateAppointmentRequest(BaseModel):
  id: Optional[str] = None
  service_id: Optional[str] = None
  date: Optional[datetime.date] = None 
  hour: Optional[datetime.time] = None
  is_notifiable: Optional[bool] = None