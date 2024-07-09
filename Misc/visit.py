from sqlmodel import SQLModel, Field, create_engine, Session, select, MetaData
from typing import Optional


class visit(SQLModel, table=True):
    code : int = Field(default=None, primary_key=True)
    city: str
    month: str
    year: Optional[int] = None

vist1 = visit(code=4, city="Multan", month="Dec", year="")


# temp = Visit.city=='Karachi'
# print(temp)
engine =create_engine("postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require")


SQLModel.metadata.create_all(engine) # database create.



#insert record
with Session(engine) as insertrecord:
    insertrecord.add(vist1)
    insertrecord.commit()
    insertrecord.close()

# to retrive the record
# with Session(engine) as retrive:
#     statement = select(visit).where(visit.city=="Karachi") # select * from visit
#     result = retrive.exec(statement).all()
#     print(result)


# Need to Discuss example of Class and Instance
#Visit = visit(code=4, city='Karachi', month='October', year = 1980)

# using col
#all()
#first()
#one()