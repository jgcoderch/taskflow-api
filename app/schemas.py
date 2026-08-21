from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool

model_config = {"from_attributes": True}


class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str

    