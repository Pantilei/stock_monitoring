from pydantic import BaseModel, EmailStr
from typing import Optional


# Share properties
class UserBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    active: Optional[str] = None
    is_superuser: Optional[bool] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str
    email: EmailStr


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: str


# Properties shared by models stored in db
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties to store in db
class UserInDB(UserInDBBase):
    hashed_password: str
