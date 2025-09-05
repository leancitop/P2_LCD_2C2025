# presentation.py - decorador de presentación
# Contiene funciones para formatear la descripción de las bebidas.
from collections import Counter

def format_description(beverage):
    description = beverage.get_description()
    parts = [p.strip() for p in description.split(",")]
    counts = Counter(parts)
    
    formatted = []
    for cond, count in counts.items():
        if count == 1:
            formatted.append(cond)
        elif count == 2:
            formatted.append(f"Double {cond}")
        elif count == 3:
            formatted.append(f"Triple {cond}")
        else:
            formatted.append(f"{count}x {cond}")
    
    return ", ".join(formatted)
