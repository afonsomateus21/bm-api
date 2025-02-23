from fastapi import APIRouter, Request, HTTPException, Depends
from starlette import status
from .validators import CreateAppointmentRequest
from routers.user.services import user_dependency
from .services import check_if_date_and_hour_are_available, get_user_for_appointment, get_service_for_appointment, individual_serial
from .models import Appointment, AppointmentProfessional, AppointmentCustomer, AppointmentService
from config.database import appointments_collection
from bson import ObjectId

appointments_router = APIRouter(prefix="/appointments", tags=["Appointments"])

@appointments_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_appointment(create_appointment_request: CreateAppointmentRequest, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  if check_if_date_and_hour_are_available(create_appointment_request.date, create_appointment_request.hour, create_appointment_request.professional_id, create_appointment_request.customer_id) is False:
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
    id=str(professional["_id"]),
    first_name=professional["first_name"],
    last_name=professional["last_name"]
  )

  appointment_customer = AppointmentCustomer(
    id=str(customer["_id"]),
    first_name=customer["first_name"],
    last_name=customer["last_name"]
  )

  appointment_service = AppointmentService(
    id=str(service["_id"]),
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