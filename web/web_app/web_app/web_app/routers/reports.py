# routers/reports.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List
from datetime import date
from ..database import get_session
from ..models import Sales, Inventory

router = APIRouter()

@router.get("/")
async def get_reports(report_type: str, start_date: date, end_date: date, session: Session = Depends(get_session)):
    if report_type == "sales":
        records = session.exec(
            select(Sales).where(Sales.sales_date.between(start_date, end_date))
        ).all()
    elif report_type == "inventory":
        records = session.exec(
            select(Inventory).where(Inventory.inventory_date.between(start_date, end_date))
        ).all()
    else:
        raise HTTPException(status_code=400, detail="Invalid report type")

    return records
# @router.get("/")
# async def get_reports(report_type: str = Query(default=None), start_date: date = Query(default=None), end_date: date = Query(default=None), session: Session = Depends(get_session)):
#     if not report_type:
#         raise HTTPException(status_code=400, detail="Missing Report")
    
#     if report_type == "sales":
#         records = session.exec(
#             select(Sales).where(Sales.sales_date.between(start_date, end_date))
#         ).all()
#         print(records)
#     elif report_type == "inventory":
#         records = session.exec(
#             select(Inventory).where(Inventory.inventory_date.between(start_date, end_date))
#         ).all()
#         print(records)
#     else:
#         raise HTTPException(status_code=400, detail="Invalid report type")

#     return records
