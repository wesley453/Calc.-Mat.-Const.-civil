import math

# Regras de dosagem de concreto por tipo de elemento estrutural
REGRAS_FCK = {
    "viga_pilar": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59},
    "baldrame": {"fck": 20, "cimento_por_m3": 7.0, "areia_por_m3": 0.66, "brita_por_m3": 0.60},
    "laje_25": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59},
    "laje_30": {"fck": 30, "cimento_por_m3": 9.0, "areia_por_m3": 0.48, "brita_por_m3": 0.55},
}

def calcular_volume(largura: float, altura: float, comprimento: float) -> float:
    """
    Calcula o volume de um elemento estrutural em m³.
    """
    return largura * altura * comprimento

def calcular_materiais(tipo: str, volume: float) -> dict:
    """
    Calcula a quantidade de materiais necessários para um determinado tipo de concreto.
    
    Args:
        tipo (str): Tipo de elemento estrutural (ex: 'viga_pilar', 'baldrame').
        volume (float): Volume em m³.
    
    Returns:
        dict: Quantidades de cimento, areia e brita, além do fck e volume total.
    """
    if tipo not in REGRAS_FCK:
        raise ValueError(f"Tipo '{tipo}' não encontrado. Tipos válidos: {list(REGRAS_FCK.keys())}")

    config = REGRAS_FCK[tipo]
    volume_total = volume * 1.05  # acréscimo de 5% para perdas

    cimento = math.ceil(volume_total * config["cimento_por_m3"])
    areia = round(volume_total * config["areia_por_m3"], 2)
    brita = round(volume_total * config["brita_por_m3"], 2)

    return {
        "tipo": tipo,
        "fck": config["fck"],
        "volume_total": round(volume_total, 2),
        "cimento": cimento,
        "areia": areia,
        "brita": brita
    }
