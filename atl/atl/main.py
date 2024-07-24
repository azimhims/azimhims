import logging
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session


from .models import atldata, engine
from .data import process_data


logging.basicConfig()
logging.getLogger("sqlmodel").setLevel(logging.INFO)

app = FastAPI()

# @app.on_event("startup")
# def on_startup():
    #SQLModel.metadata.create_all(engine)

@app.post("/insertrecord/")
def insert_record(record: atldata):
    print(record)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(record)
        session.commit()
        session.refresh(record)
    return record

    
    
    
    

    