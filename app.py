import streamlit as st

st.title("Simulador de Neurônio (Perceptron)")

col1, col2 = st.columns([1, 2])

with col1:

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
    
    st.subheader("Pesos")
    
    peso_bom = st.slider("Peso do Bom", -2.0, 2.0, 1.0, 0.1)
    peso_ruim = st.slider("Peso do Ruim", -2.0, 2.0, -1.0, 0.1)
    peso_neutro = st.slider("Peso do Neutro", -2.0, 2.0, 0.0, 0.1)
    
    st.subheader("Bias")
    
    bias = st.slider("Bias", -2.0, 2.0, 0.0, 0.1)

# --- CÁLCULO DA SOMA ---
soma = (
    int(bom) * peso_bom +
    int(ruim) * peso_ruim +
    int(neutro) * peso_neutro +
    bias
)

st.subheader("Soma ponderada")

st.write(soma)

import math

# --- FUNÇÃO SIGMOID ---
saida = 1 / (1 + math.exp(-soma))

st.subheader("Saída (sigmoid)")

st.write(saida)

st.write("Estado atual:")
st.write({
    "inputs": {
        "bom": int(bom),
        "ruim": int(ruim),
        "neutro": int(neutro)
    },
    "pesos": {
        "bom": peso_bom,
        "ruim": peso_ruim,
        "neutro": peso_neutro
    },
    "bias": bias
})
