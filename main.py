import streamlit as st
import numpy as np
import pandas as pd

#st.markdown("<h1 style='color: red;'>CALCULANDO MÉTODOS NUMÉRICOS</h1>", unsafe_allow_html=True)
st.title("\n\n\n\nCALCULANDO MÉTODOS NUMÉRICOS")
st.markdown("-------")
st.subheader("Bienvenidos a Calculando métodos numéricos ")

st.markdown("""\nEn la ingeniería y la computación, los Métodos Numéricos se erigen como el cimiento de innumerables aplicaciones, 
            desempeñando un papel en la resolución de problemas complejos que abarcan desde la simulación de fenómenos
            físicos hasta la optimización de algoritmos. En CALCULANDO MÉTODOS NUMÉRICOS, nos permíte calcular y dar  
            solución a cada uno de estos problemas, pues somos una plataforma especializada para aquellos que buscan comprender y aplicar estos
            métodos de manera rigurosa""")
st.markdown("-------")
st.subheader("Equipo de trabajo")
col1, col2 =st.columns([2,1])
col1.image("https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/rts.png", width=200, caption='Reinel Tabares')

col1.image("https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/jpd.png", width=200, caption='Piña')
col1.image("https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/rts.png", width=200, caption='Santiago Loaiza')
col2.image("https://lh3.googleusercontent.com/a/ACg8ocJLsh9d7XI0twkQezmylx3qx-UwwarUMN0Cz6hqwZPEMZKA=s458-c-no", width=200, caption='Mariana Tafur')
st.subheader("Página del curso")
url = "https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/intro.html"
st.markdown(f"[Métodos_numéricos_y_optimización]({url})")

st.subheader("Manual de usuario")
st.markdown(f"[Guía_de_funcionamiento]({url})")
#st.success("This is a success message!!!")
#st.info("This is a info message!!!")
#st.warning("This is a warning message!!!")
#st.error("This is a error message!")
#st.exception("This is a exception message")
