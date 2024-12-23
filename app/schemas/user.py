from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True


class CreateUser(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_superuser: bool

    class Config:
        orm_mode = True
