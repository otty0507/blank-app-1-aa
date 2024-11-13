# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# @st.cache(suppress_st_warning=True)
def main():
    params = st.experimental_get_query_params()
    st.text(params)
    id=params.get('id')
    st.text(id)
    st.text('https://docs.google.com/spreadsheets/d/'+id+'/edit?usp=sharing')
    url = 'https://docs.google.com/spreadsheets/d/'+id+'/edit?usp=sharing'

    conn = st.connection("gsheets", type=GSheetsConnection)

    data = conn.read(spreadsheet=url, usecols=[0, 1])
    st.dataframe(data)
main()