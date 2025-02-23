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
  date: datetime.date
  hour: datetime.time
  is_notifiable: bool