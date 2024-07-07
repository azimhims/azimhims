from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional


class Dating(SQLModel, table=True):
    code: int = Field(default=None,primary_key=True)
    Desc: str


dt1 = Dating(code=1, Desc="First self test")
dt2 = Dating(code =2, Desc="Second self test")

engine = create_engine("postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require")

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(dt1)
    session.add(dt2)
    session.commit()
    
with Session(engine) as read:
    query = select(dating)
    db = read.exec(query).all()
    print(db)