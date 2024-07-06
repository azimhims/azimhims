# streamlit_app.py
import streamlit as st
import requests
import producer
import pathlib
import json
import asyncio
#=========================================================================================================================================================================
#BASE_URL = "http://localhost:8008"
#BASE_URL = "http://backend:8008"
BASE_URL = "http://localhost:8000"
#=========================================================================================================================================================================
def main():
    # Delete the cache.json file
    cache_file = pathlib.Path("cache.json")
    if cache_file.exists():
        cache_file.unlink()
 
    st.title("Data Portal For OMC")
    
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'menu_option' not in st.session_state:
        st.session_state.menu_option = "Sales"

    if st.session_state.logged_in:
        menu_form()
    else:
        menu = ["Home", "Login", "Sign Up"]
        choice = st.sidebar.selectbox("Menu", menu)
        
        if choice == "Home":
            st.subheader("Home")

        elif choice == "Login":
            login()

        elif choice == "Sign Up":
            sign_up()
#=========================================================================================================================================================================
def login():
    st.subheader("Login")
    user_id = st.text_input("UserID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(f"{BASE_URL}/auth/login", json={"user_id": user_id, "password": password})
        if response.status_code == 200:
            st.success("Login Successful")
            st.session_state.logged_in = True
            menu_form()
        else:
            st.error("Invalid credentials")
#=========================================================================================================================================================================
def sign_up():
    st.subheader("Sign Up")
    name = st.text_input("Name")
    company_name = st.text_input("Company Name")
    user_id = st.text_input("UserID")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirmed_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        data = {
            "name": name,
            "company_name": company_name,
            "user_id": user_id,
            "email": email,
            "password": password,
            "confirmed_password": confirmed_password
        }
        
        response = requests.post(f"{BASE_URL}/signup", json=data)
        print("name",name)
        print("Status Code:", response.status_code)
        st.write("Request URL:", response.url)
        asyncio.run(producer.send_message(name))

        if response.status_code == 200 or response.status_code == 203:
            try:
                response_json = response.json()
                st.success("User created successfully")
                
                json_data = json.dumps(data, indent=4)
                st.write("Request Data:")
                st.write(json_data)
            except requests.exceptions.JSONDecodeError:
                st.error("Invalid response from API")
    
 #======================================================================================================================================================================   
    
def menu_form():
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox("Choose an option", ["Sales", "Inventory", "Reports"], index=["Sales", "Inventory", "Reports"].index(st.session_state.menu_option))

    if option != st.session_state.menu_option:
        st.session_state.menu_option = option

    if option == "Sales":
        sales_form()
    elif option == "Inventory":
        inventory_form()
    elif option == "Reports":
        reports_form()
#========================================================================================================================================================================
def sales_form():
    st.subheader("Sales Form")
    sales_qty = st.number_input("Sales Quantity")
    sales_date = st.date_input("Sales Date")
    sales_location = st.text_input("Sales Location")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/sales", json={
            "sales_qty": sales_qty,
            "sales_date": sales_date.isoformat(),
            "sales_location": sales_location
        })
        if response.status_code == 200:
            st.success("Sales record added")
#==========================================================================================================================================================================
def inventory_form():
    st.subheader("Inventory Form")
    inventory = st.number_input("Inventory")
    inventory_date = st.date_input("Inventory Date")
    inventory_location = st.text_input("Inventory Location")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/inventory", json={
            "inventory": inventory,
            "inventory_date": inventory_date.isoformat(),
            "inventory_location": inventory_location
        })
        if response.status_code == 200:
            st.success("Inventory record added")
#============================================================================================================================================================================
def reports_form():
    st.subheader("Reports")
    report_type = st.selectbox("Select Report Type", ["Sales", "Inventory"])
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    if st.button("Generate Report"):
         
        response = requests.get(f"{BASE_URL}/reports", params={
            "report_type": report_type.lower(),
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        })
        if response.status_code == 200:
            report_data = response.json()
            #st.write(response.json())
            if report_data:
                st.dataframe(report_data)
            else:
                st.info("No data available for the selected range !")
        else:
            st.error("fail to generating report")
#============================================================================================================================================================================
if __name__ == '__main__':
    main()
#==========================#
    #==================#
        #==========#
