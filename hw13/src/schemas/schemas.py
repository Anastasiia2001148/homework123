from pydantic import BaseModel
from datetime import date
from typing import Optional

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: Optional[str] = None

class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: Optional[str]

    class Config:
        from_attributes = True