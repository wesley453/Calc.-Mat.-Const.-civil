import streamlit as st
from calculos import calcular_volume, calcular_materiais, recomendar_aco

st.title("🏗️ Calculadora para Construção Civil")
st.caption("Ferramenta prática para estimar materiais e aço")

# Abas
aba = st.tabs(["Calculadora", "Tabela de Referência"])

# ---------------------------
# Aba 1: Calculadora
# ---------------------------
with aba[0]:
    st.subheader("Informe as dimensões e o tipo de elemento estrutural")

    largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.1)
    comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)

    tipo = st.selectbox(
        "Tipo de elemento",
        ["viga_pilar", "baldrame", "laje_25", "laje_30"]
    )

    if st.button("Calcular"):
        try:
            vol = calcular_volume(largura, altura, comprimento)
            materiais = calcular_materiais(tipo, vol)
            recomendacao = recomendar_aco(tipo, vol)

            st.success(
                f"""
                📐 Volume total: {materiais['volume_total']} m³  
                🏗️ Fck: {materiais['fck']} MPa  
                🧱 Cimento: {materiais['cimento']} sacos  
                🏖️ Areia: {materiais['areia']} m³  
                🪨 Brita: {materiais['brita']} m³  
                🔩 Aço recomendado: {recomendacao['aco']}  
                📏 Bitola sugerida: {recomendacao['bitola']}
                """
            )
        except Exception as ex:
            st.error(f"Erro: {ex}")

# ---------------------------
# Aba 2: Tabela de Referência
# ---------------------------
with aba[1]:
    st.subheader("📊 Tabela de Referência")

    st.table({
        "Elemento": ["Viga/Pilar", "Baldrame", "Laje 25 cm", "Laje 30 cm"],
        "Fck (MPa)": [25, 20, 25, 30],
        "Aço recomendado": ["CA-50", "CA-50", "CA-25", "CA-25"],
        "Bitola sugerida": ["10–20 mm", "8–12.5 mm", "6–10 mm", "8–12.5 mm"]
    })
