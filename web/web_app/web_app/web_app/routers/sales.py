# routers/sales.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_session
from ..models import Sales

router = APIRouter()

@router.post("/")
async def create_sale(sale: Sales, session: Session = Depends(get_session)):
    session.add(sale)
    session.commit()
    return sale
