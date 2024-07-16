from sqlmodel import SQLModel, Session, create_engine, Field, Relationship, select
from typing import Optional

class Team2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sport_type: str
    desc: str
    players: list["Player2"] = Relationship(back_populates="team")

class Player2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    category: str
    team_id: Optional[int] = Field(default=None, foreign_key="team2.id")
    team: Optional[Team2] = Relationship(back_populates="players")

DATABAE_URL = "postgresql://testdb_owner:Gxf49mATunVW@ep-shy-cake-a1jkjuiw.ap-southeast-1.aws.neon.tech/testdb?sslmode=require"
engine = create_engine(DATABAE_URL)

def create_tables():
    SQLModel.metadata.create_all(engine)

def insert_record():
    teams = []
    teams.append(Team2(sport_type="Cricket", desc="Islamabad United"))
    teams.append(Team2(sport_type="Cricket", desc="Karachi King"))

    with Session(engine) as session:
        for team in teams:
            merged_team = session.merge(team)
            session.commit()
            shd = Player2(name="Shadab Khan", country="Pakistan", category="Platinum", team=merged_team)
            nshah = Player2(name="Naseem Shah", country="Pakistan", category="Platinum", team=merged_team)
            azkhan = Player2(name="Azam Khan", country="Pakistan", category="Diamond", team=merged_team)
            ahales = Player2(name="Alex Hales", country="England", category="Gold", team=merged_team)
            jvince = Player2(name="James Vince", country="England", category="Diamond", team=merged_team)
            hali = Player2(name="Hassan Ali", country="Pakistan", category="Diamond", team=merged_team)
            smalik = Player2(name="Shoaib Malik", country="Pakistan", category="Gold", team=merged_team)
            kpollard = Player2(name="Kieron Pollard", country="West Indies", category="Diamond", team=merged_team)
            ikhan = Player2(name="Imran Khan", country="Pakistan", category="Guest")

            session.add_all([shd, nshah, azkhan, ahales, jvince, hali, smalik, kpollard, ikhan])
            session.commit()

            p = [shd, nshah, azkhan, ahales, jvince, hali, smalik, kpollard, ikhan]
            for i in p:
                session.refresh(i)

def read_record():
    with Session(engine) as session:
                
        statement = select(Player2,Team2).join(Team2).where(Player2.name=="Shoaib Malik")
        result = session.exec(statement).first()
        print(result)

def main():
    create_tables()
    insert_record()
    read_record()


if __name__ == "__main__":
        main()
