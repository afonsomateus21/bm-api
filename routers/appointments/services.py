import datetime
from config.database import appointments_collection, users_collection, offered_services_collection
from bson import ObjectId

def check_if_date_and_hour_are_available(date: datetime.date, hour: datetime.time, professional_id: str, customer_id: str):
    appointment = appointments_collection.find_one({
      "date": date,  
      "hour": hour,
      "professional.id": ObjectId(professional_id),
      "customer.id": ObjectId(customer_id)
    })

    return appointment is None

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

def individual_serial(appointment) -> dict:
  return {
    "id": str(appointment["_id"]),
    "professional": {
      "id": str(appointment["professional"]["id"]),
      "first_name": str(appointment["professional"]["first_name"]),
      "last_name": str(appointment["professional"]["last_name"])
    },
    "service": {
      "id": str(appointment["service"]["id"]),
      "title": str(appointment["service"]["title"]),
      "photo": str(appointment["service"]["photo"]) if appointment["service"]["photo"] is not None else None
    },
    "customer": {
      "id": str(appointment["customer"]["id"]),
      "first_name": str(appointment["customer"]["first_name"]),
      "last_name": str(appointment["customer"]["last_name"])
    },
    "date": str(appointment["date"]),
    "hour": str(appointment["hour"]),
    "is_notifiable": bool(appointment["is_notifiable"])
  }


def list_serial(appointments) -> list:
  return [individual_serial(appointment) for appointment in appointments]