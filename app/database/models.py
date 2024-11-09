from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    address: str = Field(max_length=255)
    phone: str = Field(max_length=25)
    mail: Optional[str] = None
    password: str = Field(max_length=255)

    orders: list["Order"] = Relationship(back_populates="user")

class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    reference: Optional[str] = Field(default=None, unique=True)

    orders: list["Order"] = Relationship(back_populates="item")

class Order(SQLModel, table=True):
    __tablename__ = "orders"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    item_id: int = Field(foreign_key="items.id", primary_key=True)
    quantity: int

    # Definimos las relaciones
    user: User = Relationship(back_populates="orders")
    item: Item = Relationship(back_populates="orders")

class FormPetition(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str
    items: List[int]
