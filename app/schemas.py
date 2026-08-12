from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str


    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

    