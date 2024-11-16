# # # this file added with compatible modules and codes
# #
# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
#
# url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
#
# conn = st.connection("gsheets", type=GSheetsConnection)
#
# data = conn.read(spreadsheet=url, usecols=[0, 1])
# st.dataframe(data, width=400)
#
# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Sheet2", usecols=[0, 1, 2], ttl=5)
# df = df.dropna(how="all")

st.dataframe(df)
# with open( "styles.css" ) as css:
#     st.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html=True)