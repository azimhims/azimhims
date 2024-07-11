#        '''import''' 
#1.Define models 	===>pydantic
#2.Create engine 	===>sqlalchamy
#3.Create table 	===>sqlalchamy
#4.Insert record 	===>sqlalchamy
#5.Query data 		===>sqlalchamy
#6.Update data 		===>sqlalchamy
#7.Delete data 		===>sqlalchamy
#8.Commit 		===>sqlalchamy    save in database
#9.Close sessin		===>sqlalchamy

from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
class lecture(SQLModel, table=True): # metadata registered
        id: Optional[int]= Field(default=None, primary_key=True)
        subject: str
        teacher: str

lect1 = lecture(subject= 'OOPS', teacher='junaid')
lect2 = lecture(subject=" MATHI", teacher='QAISAR')

DATABAE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require"
engine = create_engine(DATABAE_URL)

SQLModel.metadata.create_all(engine) #table creating


with Session(engine) as insert_session:
        insert_session.add(lect2)
        insert_session.commit()
