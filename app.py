import streamlit as st
import os

st.title("Meta Ads Monitor v1")
st.write("If you can see this, Streamlit is working.")
st.write("DATABASE_URL exists:", bool(os.getenv("DATABASE_URL")))


