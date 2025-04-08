import streamlit as st
import requests

BASE_URL = "http://localhost:8000" 

st.header("List of clinical attributes")
st.text(" the names of the cancer types")

clin_study_id=st.text_input(label='enter clinical study id, enter to apply', help='enter the study id to get the clinical attributes:')
if clin_study_id:
    r = requests.get(f"{BASE_URL}/clinical_attribute/studyId/{clin_study_id}")
    st.json(r.json())    