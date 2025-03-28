from flask import Blueprint, request, jsonify
# from models import User
from backend.models import User

from backend.database import users_collection
from backend.auth import hash_password, verify_password, create_jwt_token

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/signup", methods=["POST"])
def signup():
    data = request.json
    existing_user = users_collection.find_one({"email": data["email"]})
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400
    
    hashed_password = hash_password(data["password"])
    user_data = {"username": data["username"], "email": data["email"], "password": hashed_password}
    result = users_collection.insert_one(user_data)
    print("Inserted User ID:", result.inserted_id)
    print("Inserted User Data:", user_data)
    return jsonify({"message": "User created successfully"}), 201

@user_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    db_user = users_collection.find_one({"email": data["email"]})
    if not db_user or not verify_password(data["password"], db_user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = create_jwt_token({"email": data["email"]})
    return jsonify({"access_token": token, "token_type": "bearer"}), 200
