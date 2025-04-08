import streamlit as st

st.header('cBio mini demo')

pages={
    "about":[st.Page("about.py",title="about")],
    "reco system":[st.Page("reco.py",title="reco system")],
    "molecular profile":[
        st.Page("mp.py", title="all molecular profile"),
        st.Page("mp_id.py", title="by id"),
    ],
    "cancer types":[
        st.Page("ctype.py",title="list of cancer types"),
    ],

    "clinical attributes":[
        st.Page("ca.py",title="clinical attributes"),
        st.Page("ca_id.py",title="by study id"),
        st.Page("ca_id_attrId.py",title="by studyId & clinicalAttrID")
    ]
}

pg=st.navigation(pages)
pg.run()