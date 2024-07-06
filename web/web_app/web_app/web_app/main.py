# main.py
from fastapi import FastAPI
from .database import init_db
from .auth import auth_router
from .routers import sales, inventory, reports
from fastapi.staticfiles import StaticFiles



app = FastAPI()



#addtional for kong services
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def on_startup():
    init_db()
@app.post("/hw")
def display():
    return "Hello World"

app.include_router(auth_router, prefix="/auth")
app.include_router(sales.router, prefix="/sales")
app.include_router(inventory.router, prefix="/inventory")
app.include_router(reports.router, prefix="/reports")

