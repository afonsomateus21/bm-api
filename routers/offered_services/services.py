def individual_serial(service) -> dict:
  return {
    "id": str(service["_id"]),
    "description": str(service["description"]),
    "category": str(service["category"]),
    "professional_id": str(service["professional_id"]),
    "duration": int(service["duration"]),
    "price": float(service["price"]),
    "title": str(service["title"]),
    "photo": str(service["photo"]),
    "active": bool(service["active"]),
  }

def list_serial(offered_services) -> list:
  return [individual_serial(service) for service in offered_services]