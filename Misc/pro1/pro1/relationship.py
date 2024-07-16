from sqlmodel import SQLModel,Session, create_engine, Field, Relationship, select
from typing import Optional

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sport_type: str
    desc: str
    #player = list["players"] = Relationship()

class Players(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:  str
    country: str
    category: str
    team_type: Optional[int]= Field(default=None, foreign_key='team.id')
    #team: Optional[int] = Relationship()

DATABAE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require"
engine = create_engine(DATABAE_URL)

def create_tables():
    SQLModel.metadata.create_all(engine)

def insert_record():
    teams=[]
    teams.append(Team(sport_type = "Cricket", desc="Islamabad United"))
    teams.append(Team(sport_type = "Cricket", desc="Karachi King"))
    
    teams_id =[]
    
    #isl = Team(sport_type = "Cricket", desc="Islamabad United")
    #khi = Team(sport_type = "Cricket", desc="Karachi King")
    
    with Session(engine) as session:
        for i in teams:
            merged_team = session.merge(i)
            session.commit()
            teams_id.append(merged_team.id)  
        
        shd = Players(name="Shadab Khan", country="Pakistan",category="Platinum",team_type=teams_id[0])
        nshah = Players(name="Naseem Shah", country="Pakistan",category="Platinum",team_type=teams_id[0])
        azkhan = Players(name="Azam Khan", country="Pakistan",category="Diamond",team_type=teams_id[0])
        ahales = Players(name="Alex Hales",country="England",category="Gold", team_type=teams_id[0])
        jvince = Players(name="James Vince",country="England",category="Diamond", team_type=teams_id[1])
        hali = Players(name="Hassan Ali",country="Pakistan",category="Diamond", team_type=teams_id[1])
        smalik = Players(name="Shoaib Malik",country="Pakistan",category="Gold", team_type=teams_id[1])
        kpollard = Players(name="Kieron Pollard",country="West Indies",category="Diamond", team_type=teams_id[1])
        ikhan = Players(name="Imran Khan",country="Pakistan",category="Guest")

                        
        session.add_all([shd,nshah,azkhan,ahales,jvince,hali,smalik,kpollard,ikhan])
        session.commit()
        p = [shd,nshah,azkhan,ahales,jvince,hali,smalik,kpollard,ikhan]
        for i in p:
            session.refresh(i)  
        
def read_record():
    with Session(engine) as session:
        statement = select(Players, Team).join(Team)
        result = session.exec(statement).first()
        print(result)









def main():
    #create_tables()
    #insert_record()
    read_record()

if __name__=="__main__":
    main()
