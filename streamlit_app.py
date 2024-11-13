# example/st_app.py

import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# @st.cache(suppress_st_warning=True)
def main():
    params = st.experimental_get_query_params()
    st.text(params)
    st.text(params.id)
    # url = "https://docs.google.com/open?id=1ZGyumlD4vl6AN4EcIUIYeDK5w_48qF2LUONQqC1KJ0E"

    # conn = st.connection("gsheets", type=GSheetsConnection)

    # data = conn.read(spreadsheet=url, usecols=[0, 1])
    # st.dataframe(data)
main()