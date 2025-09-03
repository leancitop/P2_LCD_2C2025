# test_usability.py - pruebas automáticas de usabilidad
# Contiene pruebas para verificar la usabilidad del sistema de bebidas.
from utils import build_beverage
from presentation import format_description

def test_double_mocha_whip():
    drink = build_beverage("DarkRoast", None, ["Mocha", "Mocha", "Whip"])
    assert abs(drink.cost() - (0.99 + 0.20*2 + 0.10)) < 1e-6
    assert "Mocha" in drink.get_description()
    assert format_description(drink) == "DarkRoast, Double Mocha, Whip"
