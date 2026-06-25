import pytest
from App_Concreto.calculos import calcular_volume, calcular_materiais

def test_calcular_volume():
    assert calcular_volume(2, 3, 4) == 24
    assert calcular_volume(1, 1, 1) == 1

def test_calcular_materiais_viga_pilar():
    resultado = calcular_materiais("viga_pilar", 1)
    assert resultado["fck"] == 25
    assert resultado["cimento"] > 0
    assert resultado["areia"] > 0
    assert resultado["brita"] > 0

def test_calcular_materiais_baldrame():
    resultado = calcular_materiais("baldrame", 1)
    assert resultado["fck"] == 20
    assert resultado["cimento"] > 0
    assert resultado["areia"] > 0
    assert resultado["brita"] > 0

def test_calcular_materiais_laje_30():
    resultado = calcular_materiais("laje_30", 1)
    assert resultado["fck"] == 30
    assert resultado["cimento"] > 0
    assert resultado["areia"] > 0
    assert resultado["brita"] > 0

def test_calcular_materiais_laje_25():
    resultado = calcular_materiais("laje_25", 1)
    assert resultado["fck"] == 25
    assert resultado["cimento"] > 0
    assert resultado["areia"] > 0
    assert resultado["brita"] > 0
