from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, SQLModel
from typing import List

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

class Form(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str
    items: List[int]
