import streamlit as st
from calculos import (
    calcular_volume,
    calcular_materiais,
    recomendar_aco,
    validar_dimensoes,
    calcular_volume_estaca
)

def main():
    st.title("🏗️ Calculadora para Construção Civil")
    st.caption("Ferramenta prática para estimar materiais e aço")

    # Abas
    aba = st.tabs(["Calculadora", "Tabela de Referência"])

    # ---------------------------
    # Aba 1: Calculadora
    # ---------------------------
    with aba[0]:
        st.subheader("Informe as dimensões e o tipo de elemento estrutural")

        tipo = st.selectbox(
            "Tipo de elemento",
            ["viga_pilar", "baldrame", "laje_25", "laje_30", "fundacao", "bloco_alvenaria", "parede_estrutural", "estaca"]
        )

        if tipo == "estaca":
            st.subheader("⚙️ Defina as dimensões da estaca")
            diametro = st.number_input("Diâmetro (m)", min_value=0.0, step=0.1)
            profundidade = st.number_input("Profundidade (m)", min_value=0.0, step=0.1)

            if st.button("Calcular Estaca"):
                try:
                    validar_dimensoes(diametro, profundidade, 1)
                    vol_estaca = calcular_volume_estaca(diametro, profundidade)
                    materiais = calcular_materiais("estaca", vol_estaca)
                    recomendacao = recomendar_aco("estaca", vol_estaca)

                    st.success(
                        f"""
                        📐 Volume total: {materiais['volume_total']} m³  
                        🏗️ Fck: {materiais['fck']} MPa  
                        🧱 Cimento: {materiais['cimento']} sacos  
                        🏖️ Areia: {materiais['areia']} m³  
                        🪨 Brita: {materiais['brita']} m³  
                        🪨 Tipo de Brita: {materiais['tipo_brita']}  
                        🔩 Aço recomendado: {recomendacao['aco']}  
                        📏 Bitola sugerida: {recomendacao['bitola']}
                        """
                    )
                except Exception as ex:
                    st.error(f"Erro: {ex}")

        else:
            largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
            altura = st.number_input("Altura (m)", min_value=0.0, step=0.1)
            comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)

            if st.button("Calcular"):
                try:
                    validar_dimensoes(largura, altura, comprimento)
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
                        🪨 Tipo de Brita: {materiais['tipo_brita']}  
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
            "Elemento": ["Viga/Pilar", "Baldrame", "Laje 25 cm", "Laje 30 cm", "Fundação", "Bloco Alvenaria", "Parede Estrutural", "Estaca"],
            "Fck (MPa)": [25, 20, 25, 30, 20, 15, 25, 25],
            "Aço recomendado": ["CA-50", "CA-50", "CA-25", "CA-25", "CA-50", "CA-25", "CA-50", "CA-50"],
            "Bitola sugerida": ["10–20 mm", "8–12.5 mm", "6–10 mm", "8–12.5 mm", "12–20 mm", "4.2–6 mm", "8–12.5 mm", "12–20 mm"]
        })
