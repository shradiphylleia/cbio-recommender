import streamlit as st
import requests

BASE_URL="http://localhost:8000" 

st.subheader("Molecular profile")
st.text("list of molecular profiles")

limit=st.slider("Limit",1,100,10)
offset=st.slider("Offset", 0,100,0)
r=requests.get(f"{BASE_URL}/molecular_profile",params={"limit":limit,"offset":offset})
st.json(r.json())

