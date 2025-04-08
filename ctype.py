import streamlit as st
import requests

BASE_URL = "http://localhost:8000" 

st.header("List of cancer types")
st.text(" the names of the cancer types")

limit=st.slider("Limit", 1,100,10)
offset=st.slider("Offset", 0, 100,0)
r=requests.get(f"{BASE_URL}/cancer/types",params={"limit": limit,"offset": offset})
st.subheader("Cancer Types")
st.json(r.json())