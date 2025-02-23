from pydantic import BaseModel
import datetime
from typing import List, Optional

class AppointmentProfessional(BaseModel):
  id: str
  first_name: str
  last_name: str

class AppointmentService(BaseModel):
  id: str
  title: str
  photo: Optional[str] = None

class AppointmentCustomer(BaseModel):
  id: str
  first_name: str
  last_name: str

class Appointment(BaseModel):
  professional: AppointmentProfessional
  service: AppointmentService
  customer: AppointmentCustomer
  date: str
  hour: int
  is_notifiable: bool

  def to_dict(self):
    data = self.model_dump(by_alias=True)
    return data