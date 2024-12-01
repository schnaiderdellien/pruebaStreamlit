import streamlit as st

st.write("""
# Schnaider Coimbra Dellien
## esta es mi primera página de prueba
Esta página me ayudará a enseñar los datos que tengo y mejorar en el análisis de datos con python

también me ayudará ha hacer un porfolio
""")
number = st.slider("Pick a number", 0, 10)
date = st.date_input("Pick a date")
color = st.color_picker("Pick a color")
pets = ["Gato","Perro","Caballo","Ninfa"]
pet = st.radio("Pick a pet", pets)