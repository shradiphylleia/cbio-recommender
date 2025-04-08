import streamlit as st
import requests

BASE_URL="http://localhost:8000" 

st.subheader("Molecular profile by id")
mp_id=st.text_input(label="Enter Molecular Profile ID")
if mp_id:
    r=requests.get(f"{BASE_URL}/molecular_profile_id/{mp_id}")
    st.json(r.json())

else:
    st.write('enter vaild molecular profile id')