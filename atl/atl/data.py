import pandas as pd
from sqlmodel import SQLModel, Field, select, Session, create_engine
from typing import Optional


class atl(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key= True)
    SR_NO: str
    NTN: Optional[str] = Field(default=None)
    NAME: Optional[str] = Field(default=None)
    BUISINES_NAME: Optional[str] = Field(default="")
    CNIC: Optional[str] = Field(default=None)

def data_procesing():
     path = f"D:/fbr/sample_csv.csv"
     data = pd.read_csv(path)
    
     data['NTN'] = data['NTN'].astype(str)
     data['CNIC'] = data['NTN'].apply(lambda x: x if len(x) > 9 else None)
     data['NTN'] = data['NTN'].apply(lambda x: None if len(x) > 9 else x)
     data = data.where(pd.notnull(data), "")
     data_dict = data.to_dict(orient="records")
     return data_dict


def entered_record(engine):

    with Session(engine) as session:
            result = data_procesing()
            session.add_all([atl(**item) for item in result])
            session.commit()
            session.close()
            print("record save sucessfully")

def display_record(engine):
    with Session(engine) as read_session:
        statement = select(atl)
        result = read_session.exec(statement)
        for i in result:
            print(i)
def search_ntn(engine,temp):
    with Session(engine) as search_session:
        statement = select(atl).where(atl.NTN==temp)
        result = search_session.exec(statement)
        for i in result:
            print(i)
def main():
        DATABASE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/dataportal?sslmode=require"
        engine = create_engine(DATABASE_URL)

        SQLModel.metadata.create_all(engine)

        while True:
           print("        ")
           print("Main Menu")
           print("        ")
           print("1. Entered Record")
           print("2. Display the record")
           print("3. Search by NTN")
           print("4. Exit ")
           
           choice  = input("Enter Your Choise\n")

           if choice == '1':
            entered_record(engine)
           elif choice =='2':
            display_record(engine)
           elif choice=='3':
               temp = input("Entered the required NTN formated #######-#")
               search_ntn(engine,temp)
           elif choice=='4':
            break
           else:
                print("Invalid choice, Please re Entered")
                
# def process_data(data: pd.DataFrame) -> pd.DataFrame:
#     # Assuming 'data' is a pandas DataFrame with a column 'NTN'
#     data['NTN'] = data['NTN'].astype(str)
#     data['CNIC'] = data['NTN'].apply(lambda x: x if len(x) > 9 else None)
#     data['NTN'] = data['NTN'].apply(lambda x: None if len(x) > 9 else x)
#     data = data.where(pd.notnull(data), 0)
#     return data

if __name__ == "__main__":
   main()