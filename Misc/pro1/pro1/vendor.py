from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

class Vendor_type(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    desc: str

class Vendor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    ntn: str
    ven_type: Optional[int]= Field(default=None, foreign_key='vendor_type.id')

DATABAE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require"

engine = create_engine(DATABAE_URL)
# create table

def create_table():
    SQLModel.metadata.create_all(engine)

def insert_record():
    
    sup = Vendor_type(desc='Supplies')
    ser = Vendor_type(desc="Services") 

    with Session(engine) as session:
        # # session.add(sup)
        # # session.add(ser)
        # # session.commit()
    
        # # hp = Vendor(name="HP", address='Karachi',ntn='0124567-1',ven_type=sup.id)
        # # ufone = Vendor(name="Pakistan Telecommunication", address='Islamabad', ntn='0124644-5', ven_type=ser.id)
        # zong = Vendor(name="Chine Telecommunication", address='Islamabad', ntn='01234567-1', ven_type=ser.id)
        # # session.add(hp)
        # # session.add(ufone)
        # session.add(zong)
        # session.commit()
        # # session.refresh(hp)
        # # session.refresh(ufone)
        # session.refresh(zong)
        # # print(hp)
        # # print(ufone)
        # print(zong)
        
        query = select(Vendor, Vendor_type).join(Vendor_type).where(Vendor_type.desc=='Services').offset(1).limit(1)
        result = session.exec(query).all()
        print(result)

        





def main():
    create_table()
    insert_record()







if __name__=="__main__":
    main()