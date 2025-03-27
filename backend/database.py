from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)


db = client["users_db"]  # ✅ Correct database name
users_collection = db["users_details"]  # ✅ Correct collection name

# Print users to verify the connection
users = list(users_collection.find({}, {"_id": 0}))  # Exclude ObjectId for readability
print("Users in DB:", users)
