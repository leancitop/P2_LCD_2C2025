# utils.py (nuevo archivo) - construcción de bebidas (simplificado)
# Contiene funciones utilitarias para construir bebidas con condimentos.
from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy

def build_beverage(base, size=None, condiments=None):
    # 1. Crear bebida base
    bases = {"Espresso": Espresso, "DarkRoast": DarkRoast, "HouseBlend": HouseBlend}
    beverage = bases[base]()
    
    # 2. Setear tamaño si corresponde
    if size and hasattr(beverage, "set_size"):
        beverage.set_size(size)
    
    # 3. Aplicar condimentos
    condiments_map = {"Mocha": Mocha, "Whip": Whip, "Soy": Soy}
    if condiments:
        for c in condiments:
            beverage = condiments_map[c](beverage)
    
    return beverage


drink = build_beverage("DarkRoast", "Venti", ["Mocha", "Mocha", "Whip"])
print(drink.get_description(), drink.cost())
