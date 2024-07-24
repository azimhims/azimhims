import streamlit as st 
import pathlib
import pandas as pd
from atl.data import process_data
from sqlmodel import SQLModel, create_engine, Session
from atl.models import atldata, engine
import requests
cache_file = pathlib.Path("cache.json")


st.button("send data")
if st.button:
    path = f"D:/fbr/sample_csvv.csv"
    taxpayer_data = pd.read_csv(path)
    result = process_data(taxpayer_data)
    result_dict = result.to_dict(orient="records")
    #response = requests.post(f"{BASE_URL}/auth/login", json={"user_id": user_id, "password": password})
    #with Session(engine) as session:
    for record in result_dict:
        print(record)
        response = requests.post(f"http://127.0.0.1:8000/insertrecord/",json=record)
        print(response)
            
            
    #         new_record = atllis(**record)
    #         session.add(new_record)
    #     session.commit()
        
    # return result_dict
