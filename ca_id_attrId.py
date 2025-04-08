import streamlit as st
import requests

BASE_URL = "http://localhost:8000" 

st.header("List of clinical attributes by study id and clincial attribute id")

limit=st.slider("Limit", 1,100,10)
offset=st.slider("Offset", 0, 100,0)

study_id=st.text_input(label='enter study id',help='enter study id, press to apply')
clinical_attribute_id=st.text_input(label='enter clinical-attribute id',help='enter clincial attribute id, press to apply')


if st.button(label='get clinical attributes'):
    if study_id and clinical_attribute_id:
        r=requests.get(f"{BASE_URL}/clinical/attribute/studyId/{study_id}/clinicalAttributeId/{clinical_attribute_id}",params={"limit": limit,"offset": offset})
        st.subheader("Cancer Types")
        if r.status_code==200:
            st.json(r.json())
        else:
            st.write('enter valid values')