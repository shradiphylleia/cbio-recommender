import streamlit as st

st.header('reco system')

pages={
    "about":[st.Page("about.py",title="about")],
    "reco system":[st.Page("reco.py",title="reco system")]
}

pg=st.navigation(pages)
pg.run()