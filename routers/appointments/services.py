import datetime
from config.database import appointments_collection, users_collection, offered_services_collection
from bson import ObjectId

def check_if_date_and_hour_are_available(date: str, hour:int, professional_id: str, customer_id: str):
    professional_object_id = ObjectId(professional_id)
    customer_object_id = ObjectId(customer_id)

    existing_appointment = appointments_collection.find_one({
      "date": date,
      "hour": hour,
      "$or": [
        {"professional._id": professional_object_id},
        {"customer._id": customer_object_id}
      ]
    })

    return existing_appointment is None

def get_user_for_appointment(id: str):
  user = users_collection.find_one({
    "_id": ObjectId(id)
  })

  return user

def get_service_for_appointment(id: str):
  service = offered_services_collection.find_one({
    "_id": ObjectId(id)
  })

  return service


def serialize_appointment(appointment):
  appointment["_id"] = str(appointment["_id"])
  
  appointment["professional"]["_id"] = str(appointment["professional"]["_id"])
  appointment["customer"]["_id"] = str(appointment["customer"]["_id"])
  appointment["service"]["_id"] = str(appointment["service"]["_id"])
  
  return appointment

def individual_serial(appointment) -> dict:
  return {
    "id": str(appointment["_id"]),
    "professional": {
      "_id": str(appointment["professional"]["_id"]),
      "first_name": str(appointment["professional"]["first_name"]),
      "last_name": str(appointment["professional"]["last_name"])
    },
    "service": {
      "_id": str(appointment["service"]["_id"]),
      "title": str(appointment["service"]["title"]),
      "photo": str(appointment["service"]["photo"]) if appointment["service"]["photo"] is not None else None
    },
    "customer": {
      "_id": str(appointment["customer"]["_id"]),
      "first_name": str(appointment["customer"]["first_name"]),
      "last_name": str(appointment["customer"]["last_name"])
    },
    "date": str(appointment["date"]),
    "hour": str(appointment["hour"]),
    "is_notifiable": bool(appointment["is_notifiable"])
  }


def list_serial(appointments) -> list:
  return [individual_serial(appointment) for appointment in appointments]