from fastapi import APIRouter, Request, HTTPException, Depends
from starlette import status
from .validators import CreateAppointmentRequest, UpdateAppointmentRequest
from routers.user.services import user_dependency
from .services import check_if_date_and_hour_are_available, get_user_for_appointment, get_service_for_appointment, individual_serial, serialize_appointment, list_serial
from .models import Appointment, AppointmentProfessional, AppointmentCustomer, AppointmentService
from config.database import appointments_collection
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

appointments_router = APIRouter(prefix="/appointments", tags=["Appointments"])

@appointments_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_appointment(create_appointment_request: CreateAppointmentRequest, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  if check_if_date_and_hour_are_available(
    create_appointment_request.date, 
    create_appointment_request.hour, 
    create_appointment_request.professional_id, 
    create_appointment_request.customer_id
  ) is False:
    raise HTTPException(status_code=409, detail="This date and hour are unavailable.")
  
  professional = get_user_for_appointment(create_appointment_request.professional_id)

  if professional is None:
    raise HTTPException(status_code=404, detail="Professional not found.")
  
  customer = get_user_for_appointment(create_appointment_request.customer_id)

  if customer is None:
    raise HTTPException(status_code=404, detail="Customer not found.")
  
  service = get_service_for_appointment(create_appointment_request.service_id)

  if service is None:
    raise HTTPException(status_code=404, detail="Service not found.")
  
  appointment_professional = AppointmentProfessional(
    _id=ObjectId(professional["_id"]),
    first_name=professional["first_name"],
    last_name=professional["last_name"]
  )

  appointment_customer = AppointmentCustomer(
    _id=ObjectId(customer["_id"]),
    first_name=customer["first_name"],
    last_name=customer["last_name"]
  )

  appointment_service = AppointmentService(
    _id=ObjectId(service["_id"]),
    title=service["title"],
    photo=service["photo"]
  )
  
  create_appointment_model = Appointment(
    professional=appointment_professional,
    customer=appointment_customer,
    service=appointment_service,
    date=create_appointment_request.date,
    hour=create_appointment_request.hour,  
    is_notifiable=create_appointment_request.is_notifiable
  )

  result = appointments_collection.insert_one(create_appointment_model.to_dict())

  appointment_created = appointments_collection.find_one({ "_id": result.inserted_id })

  return individual_serial(appointment_created)

@appointments_router.put("/{appointment_id}", status_code=status.HTTP_200_OK)
async def update_appointment(appointment_id: str, update_appointment_request: UpdateAppointmentRequest, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  try:
    appointment = appointments_collection.find_one({"_id": ObjectId(appointment_id)})
    if appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found.")
  except:
    raise HTTPException(status_code=400, detail="Invalid appointment ID.")

  update_data = {}
  
  if update_appointment_request.date is not None or update_appointment_request.hour is not None:
    new_date = update_appointment_request.date or appointment["date"]
    new_hour = update_appointment_request.hour or appointment["hour"]
    
    existing_appointment = appointments_collection.find_one({
      "_id": {"$ne": ObjectId(appointment_id)},
      "date": new_date,
      "hour": new_hour,
      "$or": [
        {"professional._id": appointment["professional"]["_id"]},
        {"customer._id": appointment["customer"]["_id"]}
      ]
    })
      
    if existing_appointment:
      raise HTTPException(status_code=409, detail="This date and hour are unavailable.")
      
    if update_appointment_request.date is not None:
      update_data["date"] = update_appointment_request.date
    if update_appointment_request.hour is not None:
      update_data["hour"] = update_appointment_request.hour

  if update_appointment_request.service_id is not None:
    service = get_service_for_appointment(update_appointment_request.service_id)
    if service is None:
      raise HTTPException(status_code=404, detail="Service not found.")
      
    update_data["service"] = {
      "_id": ObjectId(service["_id"]),
      "title": service["title"],
      "photo": service["photo"]
    }

  if update_appointment_request.is_notifiable is not None:
    update_data["is_notifiable"] = update_appointment_request.is_notifiable

  if not update_data:
    raise HTTPException(status_code=400, detail="No data provided for update.")

  result = appointments_collection.update_one(
    {"_id": ObjectId(appointment_id)},
    {"$set": update_data}
  )

  if result.modified_count == 0:
    raise HTTPException(status_code=400, detail="Failed to update appointment.")

  updated_appointment = appointments_collection.find_one({"_id": ObjectId(appointment_id)})
  return individual_serial(updated_appointment)

@appointments_router.get("/{appointment_id}", status_code=status.HTTP_200_OK)
async def get_appointment(appointment_id: str, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  appointment = appointments_collection.find_one({ "_id": ObjectId(appointment_id) })

  if appointment is None:
    raise HTTPException(status_code=404, detail="Appointment not found.")
  
  serialized_appointment = serialize_appointment(appointment)
  
  return jsonable_encoder(serialized_appointment)

@appointments_router.get("/", status_code=status.HTTP_200_OK)
async def list_appointments(current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  appointments = list_serial(appointments_collection.find())

  return appointments

@appointments_router.delete("/{appointment_id}", status_code=status.HTTP_200_OK)
async def remove_appointment(appointment_id: str, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  result = appointments_collection.delete_one({ "_id": ObjectId(appointment_id) })

  if result.deleted_count == 0:
    raise HTTPException(status_code=404, detail="Appointment not found.")
  
  return { "success": True, "message": "Appointment successfully removed." }