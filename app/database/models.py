from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    address: str = Field(max_length=255)
    phone: str = Field(max_length=25)
    email: Optional[str] = Field(default=None)
    state: Optional[str] = Field(default=None)
    document: Optional[str] = Field(default=None)

    orders: list["Order"] = Relationship(back_populates="user")

class Item(SQLModel, table=True):
    __tablename__ = "items"

    name: str = Field(primary_key=True)

    orders: list["Order"] = Relationship(back_populates="item")

class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    item_id: Optional[str] = Field(default=None, foreign_key="items.name")

    user: User = Relationship(back_populates="orders")
    item: Item = Relationship(back_populates="orders")

class FormPetition(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str
    items: List[int]
