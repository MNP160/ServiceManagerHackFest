import streamlit as st
from db import *
import pandas as pd



def main():
    """Simple Service Manager App"""
    st.title("Service Manager App")
    username = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.button("Login",'alabala'):
        result = check_user_exists(username,password)
        if result:
            while result:

                if st.button("View Services", '2'):
                    st.subheader("Service Table")
                    services=get_all_services()
                    df=pd.DataFrame(services, columns=["Name, Url"])
                    st.dataframe(df)     
    else :
			
        st.warning("Incorrect Username/Password")







if __name__ == '__main__':
	main()