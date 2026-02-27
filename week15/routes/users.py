from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()

store = UserStore("users.db")


@router.get("/")
def get_users():
    return store.load()


@router.post("/")
def create_user(user: UserCreate):

    users = store.load()

    new_id = 1 if not users else max(
        u["id"] for u in users) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    store.save(users)

    return new_user


@router.get("/{user_id}")
def get_user(user_id: int):

    user = store.find_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}")
def update_user(user_id: int,
                updated: UserCreate):

    success = store.update_user(
        user_id,
        updated.dict()
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete_user(user_id: int):

    success = store.delete_user(user_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User deleted"}
