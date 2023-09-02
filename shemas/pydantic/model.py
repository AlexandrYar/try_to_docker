from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    email: str
    login: str
    passwordHash: str
    role: str
    age: int = None