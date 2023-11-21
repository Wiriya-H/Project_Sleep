import streamlit as st

col1, col2, col3 = st.columns([1.5, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./pic/44.png")

with col3:
    st.write("")
    
    
html_1 = """
<div style="background-color:#0E1117;border-top: 3px solid #ffffff;border-bottom: 3px solid #ffffff;">
<center><h4>Wiriya Hemmala 64/44 007</h4></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")   