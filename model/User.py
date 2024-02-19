from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_lenght=50, max_length=250)
    password: str = Field(min_length=8, max_length=20)
