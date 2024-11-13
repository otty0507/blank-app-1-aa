# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# @st.cache(suppress_st_warning=True)
def main():
    params = st.experimental_get_query_params()
    st.text(params)
    st.text(params['id'])
    id=params['id'][0]
    url = f"https://docs.google.com/spreadsheets/d/{id}"

    conn = st.connection("gsheets", type=GSheetsConnection)

    data = conn.read(spreadsheet=url, usecols=[0, 1])
    st.dataframe(data)
main()