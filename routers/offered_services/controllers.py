from fastapi import APIRouter, HTTPException, Query
from routers.user.services import user_dependency
from starlette import status
from .validators import CreateOfferedServiceRequest, UpdateOfferedServiceRequest, FileUploadRequest
from .models import OfferedService
from config.database import offered_services_collection
from routers.user.validators import UserType
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from .services import list_serial
from supabase import create_client, Client
from starlette.config import Config

config = Config(".env")

SUPABASE_SERVICE_ROLE_KEY = config("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_PROJECT_URL = config("SUPABASE_PROJECT_URL")

offered_services_router = APIRouter(prefix="/service", tags=["Service"])
supabase: Client = create_client(SUPABASE_PROJECT_URL, SUPABASE_SERVICE_ROLE_KEY)

@offered_services_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_service(create_service_request: CreateOfferedServiceRequest, current_user: user_dependency):
  if str(current_user["type"]) != UserType.ADMIN:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  create_service_model = OfferedService(
    title=create_service_request.title,
    description=create_service_request.description,
    category=create_service_request.category,
    professional_id=create_service_request.professional_id,
    duration=create_service_request.duration,
    price=create_service_request.price,
    photo=create_service_request.photo,
    active=create_service_request.active
  )

  create_service_model.professional_id = ObjectId(create_service_model.professional_id)

  offered_services_collection.insert_one({
    **dict(create_service_model),
    "professional_id": ObjectId(create_service_model.professional_id)
  })

  return create_service_request

@offered_services_router.post("/upload-photo", status_code=status.HTTP_200_OK)
async def upload_photo(request: FileUploadRequest):
  try:
    file_path = f"services/{request.file_name}"

    response = supabase.storage.from_("services").create_signed_upload_url(file_path)

    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"]["message"])

    return {"url": response["signedUrl"], "file_path": file_path}

  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not upload the image.")
  
@offered_services_router.put("/{id}", status_code=status.HTTP_200_OK)
async def edit_service(id:str, update_service_request: UpdateOfferedServiceRequest, current_user: user_dependency):
  if str(current_user["type"]) != UserType.ADMIN:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  update_data = update_service_request.model_dump(exclude_unset=True)
  
  if "professional_id" in update_data:
    update_data["professional_id"] = ObjectId(update_data["professional_id"])

  result = offered_services_collection.update_one(
    {"_id": ObjectId(id)}, 
    {"$set": dict(update_data)}
  )

  if result.modified_count == 0:
    raise HTTPException(status_code=400, detail="No changes were made to the service.")
  
  updated_service = offered_services_collection.find_one({"_id": ObjectId(id)})

  if updated_service is None:
    raise HTTPException(status_code=404, detail="Service not found.")

  updated_service["_id"] = str(updated_service["_id"])
  if "professional_id" in updated_service and isinstance(updated_service["professional_id"], ObjectId):
    updated_service["professional_id"] = str(updated_service["professional_id"])

  return jsonable_encoder(updated_service)

@offered_services_router.get("/", status_code=status.HTTP_200_OK)
async def list_services(current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  services = list_serial(offered_services_collection.find())

  return services

@offered_services_router.get("/professional", status_code=status.HTTP_200_OK)
async def list_services_by_professional(
  current_user: user_dependency,
  professional_id: str = Query(..., title="Professional ID", description="ID of the professional")
):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  service = offered_services_collection.find_one({ "professional_id": ObjectId(professional_id) })

  if service is None:
    raise HTTPException(status_code=404, detail="There is no service for this professional.")
  
  service["_id"] = str(service["_id"])
  service["professional_id"] = str(service["professional_id"])

  return jsonable_encoder(service)

@offered_services_router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_service(id: str, current_user: user_dependency):
  if current_user is None:
    raise HTTPException(status_code=403, detail="You are not authorized to make this action.")
  
  service = offered_services_collection.find_one({ "_id": ObjectId(id) })

  if service is None:
    raise HTTPException(status_code=404, detail="Service not found.")
  
  service["_id"] = str(service["_id"])
  service["professional_id"] = str(service["professional_id"])

  return jsonable_encoder(service)
  
@offered_services_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def remove_service(id: str, current_user: user_dependency):
  if str(current_user["type"]) != UserType.ADMIN:
    raise HTTPException(status_code=403, detail="You are not authorized to remove this service.")
  
  result = offered_services_collection.delete_one({ "_id": ObjectId(id) })

  if result.deleted_count == 0:
    raise HTTPException(status_code=404, detail="User not found.")
  
  return { "success": True, "message": "Service successfully removed." }

