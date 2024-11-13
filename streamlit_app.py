# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# @st.cache(suppress_st_warning=True)
def main():
    params = st.experimental_get_query_params()
    st.text(params)
    id=params.get('id')[0]
    st.text(id)
    st.text('https://docs.google.com/spreadsheets/d/'+str(id)+'/edit?gid=0#gid=0')
    url = 'https://docs.google.com/spreadsheets/d/'+str(id)+'/edit?gid=0#gid=0'

    conn = st.connection("gsheets", type=GSheetsConnection)

    data = conn.read(spreadsheet=url, usecols=[0, 1])
    st.dataframe(data)
main()