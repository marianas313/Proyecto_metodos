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

col1.image("https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/jpd.png", width=200, caption='Johan Piña')
col2.image("https://scontent.feoh3-1.fna.fbcdn.net/v/t39.30808-6/409127958_10219032175914038_4087875798827327043_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeG_ZrnjKpLVJY59TtoNP2zHSBAFu6uzDPxIEAW7q7MM_LkOAtDslybaY2UvK0P1K8E&_nc_ohc=TVfy7afp4WYAX_ataAR&_nc_oc=AQmFhJEX2i0VRbNPaviHBCWDsLxIUzD6mMRwtbbsqGsB-0MNvabHXqpsXk5ukOH-Mt4vmiLlbQwCCWv6Q68wNEtV&_nc_ht=scontent.feoh3-1.fna&oh=00_AfAk6bDZ1YQmsGVzzS7XHJd_S_ofrOOWb8TvTbLYMcsaog&oe=65765D12", width=200, caption='Santiago Loaiza')
col2.image("https://lh3.googleusercontent.com/a/ACg8ocJLsh9d7XI0twkQezmylx3qx-UwwarUMN0Cz6hqwZPEMZKA=s458-c-no", width=200, caption='Mariana Tafur')
st.subheader("Página del curso")
url = "https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/intro.html"
st.markdown(f"[Métodos_numéricos_y_optimización]({url})")
url2="https://publuu.com/flip-book/328994/757494"
st.subheader("Manual de usuario")
st.markdown(f"[Guía_de_funcionamiento]({url2})")
#st.success("This is a success message!!!")
#st.info("This is a info message!!!")
#st.warning("This is a warning message!!!")
#st.error("This is a error message!")
#st.exception("This is a exception message")
