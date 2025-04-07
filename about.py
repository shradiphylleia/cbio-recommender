import streamlit as st
st.title('About the recommendation system')

st.subheader('introduction')

st.text(body='In oncology,comparing similar cases can inform research and treatment strategies.This tool aims to automate that process using molecular and clinical profiles.')
st.divider()

st.subheader('current interface')
st.text(body='cbio currrently provide implementations to allow users to manually search individual patient data exploration, including mutations, copy number variations, and clinical information as well as cohort exploration, analytics, and cohort comparisons.')
st.divider()

st.subheader('proposed plan')
st.text(body='This mini implementation uses cbio api to help user find similar patients by using the interface to look for patients that e.g. are of the same cancer type, have similar mutations, or received the same treatment.')

