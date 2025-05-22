import os
import streamlit as st
import streamlit.components.v1 as components

_allow_html=True
#)
st.title("Cardápio")

#st.markdown(
 #   '<a href="http://localhost:5001/html/index.html" target="_blank">Abrir HTML</a>',
  #  unsafe_allow_html=True
#)
#st.markdown(
 #   '<a href="https://html-flask-server.onrender.com" target="_blank">Abrir HTML</a>',
  #  unsafe_allow_html=True
#)
st.markdown('[Abrir página HTML](http://localhost:8000/index.html)', unsafe_allow_html=True)