import streamlit as st

import streamlit as st

st.title("Simulador de Neurônio (Perceptron)")

st.subheader("Entradas")

bom = st.checkbox("Bom")
ruim = st.checkbox("Ruim")
neutro = st.checkbox("Neutro")

st.write("Valores atuais:")
st.write({
    "bom": int(bom),
    "ruim": int(ruim),
    "neutro": int(neutro)
})
