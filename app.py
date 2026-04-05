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

with col2:
    st.subheader("Cálculo")

    st.write("Soma:", soma)
    st.write("Saída:", saida)

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    
    # desenhar círculo (neurônio)
    circulo = plt.Circle((0.55, 0.5), 0.1, fill=False)
    ax.add_patch(circulo)
    
    # símbolo Σ
    ax.text(0.55, 0.5, "Σ", ha='center', va='center', fontsize=16)

    # coordenadas das entradas
    entradas = {
        "bom": (0.2, 0.7),
        "ruim": (0.2, 0.5),
        "neutro": (0.2, 0.3)
    }
    
    # desenhar linhas (setas simplificadas)
    for label, (x, y) in entradas.items():
        ax.annotate(
            "", 
            xy=(0.5, 0.5), 
            xytext=(x, y),
            arrowprops=dict(facecolor='blue', shrink=0.2, width=1)
        )
        ax.text(x - 0.01, y, label, ha='right', va='center')
    
    # limites e limpeza
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    st.pyplot(fig)

    
