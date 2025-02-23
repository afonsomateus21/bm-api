from pydantic import BaseModel, Field
import datetime
from typing import List, Optional
from bson import ObjectId

class PyObjectId(ObjectId):
  @classmethod
  def __get_validators__(cls):
    yield cls.validate

  @classmethod
  def validate(cls, v, handler):
    if not isinstance(v, ObjectId):
      if not ObjectId.is_valid(v):
        raise ValueError("Invalid ObjectId")
      v = ObjectId(v)
    return v

  @classmethod
  def __get_pydantic_json_schema__(cls, field_schema):
    field_schema.update(type="string")
    return field_schema

class AppointmentProfessional(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  first_name: str
  last_name: str

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    populate_by_name = True

class AppointmentService(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  title: str
  photo: Optional[str] = None

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    populate_by_name = True

class AppointmentCustomer(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  first_name: str
  last_name: str

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    populate_by_name = True

class Appointment(BaseModel):
  professional: AppointmentProfessional
  service: AppointmentService
  customer: AppointmentCustomer
  date: str
  hour: int
  is_notifiable: bool

  class Config:
    arbitrary_types_allowed = True

  def to_dict(self):
    data = self.model_dump(by_alias=True)
    data["professional"]["_id"] = ObjectId(str(data["professional"]["_id"]))
    data["service"]["_id"] = ObjectId(str(data["service"]["_id"]))
    data["customer"]["_id"] = ObjectId(str(data["customer"]["_id"]))
    return data