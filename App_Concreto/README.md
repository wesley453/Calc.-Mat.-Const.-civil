# 🏗️ Calculadora de Materiais para Construção Civil

Ferramenta desenvolvida em **Python + Streamlit** para auxiliar no cálculo de materiais e aço em obras de construção civil.  
O projeto permite estimar volumes de concreto, consumo de cimento, areia, brita, aço e também materiais de alvenaria.

---

## ✨ Funcionalidades

### 🔨 Infraestrutura e Estrutura
- Estaca (cálculo de volume cilíndrico)
- Radie
- Viga Baldrame
- Pilar
- Laje

Para cada elemento, a calculadora retorna:
- Volume total de concreto
- Consumo de cimento, areia e brita
- Tipo de brita recomendado
- Aço recomendado e bitola sugerida

---

### 🧱 Alvenaria e Fechamento
- Chapisco
- Emboço
- Reboco
- Tijolo (Bloco)

Para cada item, a calculadora retorna:
- Consumo de cimento e areia por área (m²)
- Quantidade de blocos necessários
- Volume de argamassa

---

### 📊 Tabela de Referência
- Exibe os valores de **Fck (MPa)**, tipo de aço recomendado e bitolas sugeridas para cada elemento estrutural.

---

### 🌦️ Condições Ambientais
- Data e hora atuais
- Temperatura e umidade do ar em tempo real (via API OpenWeather)

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/wesley453/Calc.-Mat.-Const.-civil.git
