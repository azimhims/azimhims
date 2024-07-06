# models.py
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional
from datetime import date

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    company_name: str
    user_id: str = Field(unique=True)
    email: str
    password: str

class Sales(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sales_qty: int
    sales_date: date
    sales_location: str

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    inventory: int
    inventory_date: date
    inventory_location: str
