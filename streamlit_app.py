# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# @st.cache(suppress_st_warning=True)
def main():
    id = st.query_params.id
    # st.text(params)
    # id=params.get('id')
    st.text(id)

    # st.text(str(st.query_params.to_dict))
    st.text('https://docs.google.com/spreadsheets/d/'+str(id)+'/edit?gid=1513024147#gid=1513024147')
    url = 'https://docs.google.com/spreadsheets/d/'+str(id)+'/edit?gid=1513024147#gid=1513024147'

    conn = st.connection("gsheets", type=GSheetsConnection)

    data = conn.read(spreadsheet=url, usecols=[0, 1])
    st.dataframe(data)
main()