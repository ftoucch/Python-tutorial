from datetime import datetime
from pydantic import BaseModel

class User(BaseModel) :
    id: int
    name: str = "john Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id" : "123",
    "signup_ts" : "2017-06-01 12:22"
}

user = User(**external_data)
print(user)