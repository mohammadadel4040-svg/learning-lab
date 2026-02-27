from fastapi import APIRouter, HTTPException
from schema import UserCreate
import json
import os

# Create router
router = APIRouter()

FILE_NAME = "users.txt"


# READ USERS FROM FILE
def read_users():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return []


# SAVE USERS
def write_users(users):

    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=2)


# GENERATE NEW ID
def get_next_id(users):

    if not users:
        return 1

    return max(user["id"] for user in users) + 1


# CREATE USER
@router.post("/")
def create_user(user: UserCreate):

    users = read_users()

    new_user = {
        "id": get_next_id(users),
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    write_users(users)

    return new_user


# GET ALL USERS
@router.get("/")
def get_users():
    return read_users()


# GET USER BY ID
@router.get("/{user_id}")
def get_user(user_id: int):

    users = read_users()

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404,
                        detail="User not found")


# UPDATE USER
@router.put("/{user_id}")
def update_user(user_id: int,
                updated: UserCreate):

    users = read_users()

    for user in users:
        if user["id"] == user_id:
            user["name"] = updated.name
            user["email"] = updated.email
            write_users(users)
            return user

    raise HTTPException(status_code=404,
                        detail="User not found")


# DELETE USER 
@router.delete("/{user_id}")
def delete_user(user_id: int):

    users = read_users()

    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404,
                        detail="User not found")
