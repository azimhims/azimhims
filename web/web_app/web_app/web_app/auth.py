# auth.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from .database import get_session
from .models import User



auth_router = APIRouter()

class UserCreate(BaseModel):
    name: str
    company_name: str
    user_id: str
    email: str
    password: str
    confirmed_password: str

    def validate_passwords(self):
        if self.password != self.confirmed_password:
            raise ValueError("Passwords do not match")

class UserLogin(BaseModel):
    user_id: str
    password: str
#--------------------------------------------------------------
#producer = Producer({'bootstrap.servers': 'your_kafka_broker'})
#--------------------------------------------------------------
@auth_router.post("/signup")
async def signup(user: UserCreate, session: Session = Depends(get_session)):
    user.validate_passwords()
    db_user = session.exec(select(User).where(User.user_id == user.user_id)).first()
    if db_user:
        print(db_user)
        raise HTTPException(status_code=400, detail="UserID already exists")
    new_user = User(**user.dict(exclude={"confirmed_password"}))
    session.add(new_user)
    session.commit()
    #-----------------------------------------------------------------------
    
    # welcome_email = user_signup_pb2.WelcomeEmail(
    #     name=user.name,
    #     email=user.email
    # )
    
    # # Produce message to Kafka
    
    #  # Produce message to Kafka
    # producer.produce('welcome_email', welcome_email.SerializeToString())
    # producer.flush()

    # producer.flush()
    #------------------------------------------------------------------------
    return {"message": "User created successfully"}

@auth_router.post("/login")
async def login(user: UserLogin, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.user_id == user.user_id)).first()
    print(db_user)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

# from kafka import Producer
# import user_signup_pb2
# producer = Producer({'bootstrap.servers':'your_kafka_broker'})