import math

# Regras de dosagem de concreto por tipo de elemento estrutural
REGRAS_FCK = {
    "viga_pilar": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59},
    "baldrame": {"fck": 20, "cimento_por_m3": 7.0, "areia_por_m3": 0.66, "brita_por_m3": 0.60},
    "laje_25": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59},
    "laje_30": {"fck": 30, "cimento_por_m3": 9.0, "areia_por_m3": 0.48, "brita_por_m3": 0.55},
}

# Regras de recomendação de aço por tipo de elemento (base simplificada da NBR 6118)
REGRAS_ACO = {
    "viga_pilar": {"aco": "CA-50", "bitola_min": "10 mm", "bitola_max": "20 mm"},
    "baldrame": {"aco": "CA-50", "bitola_min": "8 mm", "bitola_max": "12.5 mm"},
    "laje_25": {"aco": "CA-25", "bitola_min": "6 mm", "bitola_max": "10 mm"},
    "laje_30": {"aco": "CA-25", "bitola_min": "8 mm", "bitola_max": "12.5 mm"},
}

def calcular_volume(largura: float, altura: float, comprimento: float) -> float:
    """
    Calcula o volume de um elemento estrutural em m³.
    """
    return largura * altura * comprimento

def calcular_materiais(tipo: str, volume: float) -> dict:
    """
    Calcula a quantidade de materiais necessários para um determinado tipo de concreto.
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

def recomendar_aco(tipo: str, volume: float) -> dict:
    """
    Retorna recomendações de aço e bitola com base no tipo de elemento e volume.
    Ajusta bitola conforme volume (simplificação da NBR 6118).
    """
    if tipo not in REGRAS_ACO:
        raise ValueError(f"Tipo '{tipo}' não encontrado. Tipos válidos: {list(REGRAS_ACO.keys())}")

    regra = REGRAS_ACO[tipo]

    # Ajuste simplificado: quanto maior o volume, maior a bitola recomendada
    if volume <= 1.0:
        bitola = regra["bitola_min"]
    else:
        bitola = regra["bitola_max"]

    return {
        "aco": regra["aco"],
        "bitola": bitola
    }
