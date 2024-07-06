# routers/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import Inventory

router = APIRouter()

@router.post("/")
async def create_inventory(inventory: Inventory, session: Session = Depends(get_session)):
    session.add(inventory)
    session.commit()
    session.refresh(inventory)
    return inventory

@router.get("/")
async def read_inventory(session: Session = Depends(get_session)):
    inventories = session.exec(select(Inventory)).all()
    return inventories
