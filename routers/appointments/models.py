from pydantic import BaseModel
import datetime
from typing import List

class AppointmentProfessional(BaseModel):
  id: str
  name: str
  scheduled_time: List[datetime.time]

class AppointmentService(BaseModel):
  id: str
  title: str

class Appointment(BaseModel):
  professional: AppointmentProfessional
  service: str
  date: datetime.date
  hour: datetime.time
  is_notifiable: bool