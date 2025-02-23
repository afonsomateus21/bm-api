import datetime
from config.database import appointments_collection, users_collection, offered_services_collection
from bson import ObjectId

def check_if_date_and_hour_are_available(date: datetime.date, hour: datetime.time, professional_id: str, customer_id: str):
    appointment = appointments_collection.find_one({
      "date": date.isoformat(),  # Se armazenado como string no formato YYYY-MM-DD
      "hour": hour.strftime("%H:%M:%S"),  # Se armazenado como string HH:MM:SS
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