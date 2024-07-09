from sqlmodel import SQLModel, Field, create_engine, Session, select, or_
from typing import Optional
class person(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    emp_code: int
    name: str
    age: Optional[int]= None
    location: str
    education: str


# p2 = person(emp_code= 84,name='azeem', location='karachi', education='MBA')
# p3 = person(emp_code= 26,name='sajid', location='multan',age=63, education='PHD')
# p4 = person(emp_code= 51,name='taha', location='lahore', education='BS')
# p5 = person(emp_code= 37,name='mahira', location='Hyderabad',age=28, education='MBBS')
# p6 = person(emp_code= 16,name='moiz', location='Kashmir',age=45, education='BE')
# p1 = person(emp_code= 90,name='kaleem', location='Quetta',age=18, education='CA')

DATABAE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require"

engine = create_engine(DATABAE_URL)
SQLModel.metadata.create_all(engine)


# with Session(engine) as session:
#     session.add(p2)
#     session.add(p3)
#     session.add(p4)
#     session.add(p5)   
#     session.add(p6)
#     session.commit()
#     session.close()

with Session(engine) as session:
    statement = select(person).where(or_(person.age<20, person.age<30))
    result = session.exec(statement)
    for i in result:
        print(i)