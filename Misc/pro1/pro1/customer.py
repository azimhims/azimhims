from sqlmodel import SQLModel, Field, create_engine, select, Session
from typing import Optional

class Customer_type(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    desc: str

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    ntn: str
    cust_type: Optional[int] = Field(default=None,foreign_key='customer_type.id')

DATABASE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/dataportal?sslmode=require"

engine = create_engine(DATABASE_URL)
def create_table():
    SQLModel.metadata.create_all(engine)

def create_customer():
    consumer = Customer_type(desc='Consumer')
    retail_site = Customer_type(desc='Retail')
    bulk = Customer_type(desc="Bulk")

    with Session(engine) as session:
        session.add(consumer)
        session.add(retail_site)
        session.add(bulk)
        session.commit()

        ASKARI = Customer(name='Askari Filling Station', address='PhalanGoat, Karachi', ntn='0452145-1', cust_type=retail_site.id)
        ARFEEN = Customer(name='Arfeen Filling Station', address="Shahrah-e-Faisal, Karachi", ntn='01234567-8',cust_type=retail_site.id)
    
        session.add(ASKARI)
        session.add(ARFEEN)
        session.commit()
        session.refresh(ASKARI)
        session.refresh(ARFEEN)


        print("ASkri REtail sied opend:", ASKARI)
        print("Retail Site Stored :", ARFEEN)
def main():
    create_table()
    create_customer()
    

if __name__ == "__main__":
     main()
        