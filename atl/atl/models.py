from sqlmodel import SQLModel, Field, Session, create_engine
from typing import Optional

DATABASE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/dataportal?sslmode=require"

engine = create_engine(DATABASE_URL, echo=True)

# def get_session():
#     with Session(engine) as session:
#         yield session   

class atldata(SQLModel, existing_table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    SR_NO : int 
    NTN: str 
    NAME: str 
    BUSINESS_NAME: str 
    CNIC: str 


    