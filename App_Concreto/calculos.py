import math

# Regras de dosagem de concreto por tipo de elemento estrutural
REGRAS_FCK = {
    "viga_pilar": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59, "tipo_brita": "Brita 1"},
    "baldrame": {"fck": 20, "cimento_por_m3": 7.0, "areia_por_m3": 0.66, "brita_por_m3": 0.60, "tipo_brita": "Brita 1"},
    "laje_25": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59, "tipo_brita": "Brita 0"},
    "laje_30": {"fck": 30, "cimento_por_m3": 9.0, "areia_por_m3": 0.48, "brita_por_m3": 0.55, "tipo_brita": "Brita 0"},
    "fundacao": {"fck": 20, "cimento_por_m3": 7.5, "areia_por_m3": 0.65, "brita_por_m3": 0.62, "tipo_brita": "Brita 1"},
    "bloco_alvenaria": {"fck": 15, "cimento_por_m3": 5.0, "areia_por_m3": 0.70, "brita_por_m3": 0.50, "tipo_brita": "Brita 0"},
    "parede_estrutural": {"fck": 25, "cimento_por_m3": 8.5, "areia_por_m3": 0.55, "brita_por_m3": 0.58, "tipo_brita": "Brita 1"},
    "estaca": {"fck": 25, "cimento_por_m3": 8.0, "areia_por_m3": 0.57, "brita_por_m3": 0.59, "tipo_brita": "Brita 1"},
}

# Regras de recomendação de aço por tipo de elemento
REGRAS_ACO = {
    "viga_pilar": {"aco": "CA-50", "bitola_min": "10 mm", "bitola_max": "20 mm"},
    "baldrame": {"aco": "CA-50", "bitola_min": "8 mm", "bitola_max": "12.5 mm"},
    "laje_25": {"aco": "CA-25", "bitola_min": "6 mm", "bitola_max": "10 mm"},
    "laje_30": {"aco": "CA-25", "bitola_min": "8 mm", "bitola_max": "12.5 mm"},
    "fundacao": {"aco": "CA-50", "bitola_min": "12 mm", "bitola_max": "20 mm"},
    "bloco_alvenaria": {"aco": "CA-25", "bitola_min": "4.2 mm", "bitola_max": "6 mm"},
    "parede_estrutural": {"aco": "CA-50", "bitola_min": "8 mm", "bitola_max": "12.5 mm"},
    "estaca": {"aco": "CA-50", "bitola_min": "12 mm", "bitola_max": "20 mm"},
}

def validar_dimensoes(largura: float, altura: float, comprimento: float) -> None:
    """
    Valida se as dimensões são positivas e não nulas.
    """
    if largura <= 0:
        raise ValueError("A largura deve ser maior que zero.")
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    if comprimento <= 0:
        raise ValueError("O comprimento deve ser maior que zero.")

def calcular_volume(largura: float, altura: float, comprimento: float) -> float:
    """
    Calcula o volume de um elemento estrutural em m³.
    """
    return largura * altura * comprimento

def calcular_volume_estaca(diametro: float, profundidade: float) -> float:
    """
    Calcula o volume de uma estaca cilíndrica em m³.
    Fórmula: V = π * (raio²) * altura
    """
    if diametro <= 0 or profundidade <= 0:
        raise ValueError("Diâmetro e profundidade devem ser maiores que zero.")

    raio = diametro / 2
    volume = math.pi * (raio ** 2) * profundidade
    return round(volume, 3)

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
        "brita": brita,
        "tipo_brita": config.get("tipo_brita", "Brita 1")
    }

def recomendar_aco(tipo: str, volume: float) -> dict:
    """
    Retorna recomendações de aço e bitola com base no tipo de elemento e volume.
    Ajusta bitola conforme volume (simplificação da NBR 6118).
    """
    if tipo not in REGRAS_ACO:
        raise ValueError(f"Tipo '{tipo}' não encontrado. Tipos válidos: {list(REGRAS_ACO.keys())}")

    regra = REGRAS_ACO[tipo]

    if volume <= 1.0:
        bitola = regra["bitola_min"]
    else:
        bitola = regra["bitola_max"]

    return {
        "aco": regra["aco"],
        "bitola": bitola
    }