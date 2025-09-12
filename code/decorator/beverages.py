# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    VALID_SIZES = ("Tall", "Grande", "Venti")
    def __init__(self, size=None):
        self.description = "Bebida Desconocida"
        if size is None:
            self.size = "Grande"
        elif size in self.VALID_SIZES:
            self.size = size
        else:
            raise ValueError(f"Tamaño '{size}' no válido. Debe ser Tall, Grande o Venti.")

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description
    
    def set_size(self, size):
        """
        Establece el tamaño de la bebida.
        """
        if size in self.VALID_SIZES:
            self.size = size
        else:
            raise ValueError(f"Tamaño '{size}' no válido. Debe ser Tall, Grande o Venti.")

    def get_size(self):
        """
        Devuelve el tamaño de la bebida.
        """
        return self.size

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self, size=None):
        super().__init__(size)
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self, size=None):
        super().__init__(size)
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self, size=None):
        super().__init__(size)
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self, size=None):
        super().__init__(size)
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
