# schema.py
# Defines data models for user validation

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class UserCreate(BaseModel):
    name: str
    email: str
