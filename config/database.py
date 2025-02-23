from pymongo import MongoClient
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

username = quote_plus(os.getenv("DB_USERNAME"))
password = quote_plus(os.getenv("DB_PASSWORD"))

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.auyee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.bm_db

users_collection = db["users"]
offered_services_collection = db["offeredServices"]
appointments_collection = db["appointments"]