from abc import ABC, abstractmethod
from pizza import Pizza, NYStyleCheesePizza, ChicagoStyleCheesePizza, NYStyleVeggiePizza, NYStylePepperoniPizza, ChicagoStyleVeggiePizza, ChicagoStylePepperoniPizza

class PizzaStore(ABC):
    def order_pizza(self, kind: str) -> Pizza:
        pizza = self.create_pizza(kind)
        pizza.prepare(); pizza.bake(); pizza.cut(); pizza.box()
        return pizza
    @abstractmethod
    def create_pizza(self, kind: str) -> Pizza: ...

class NYPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        if kind.lower() == "cheese": return NYStyleCheesePizza()
        if kind.lower() == "veggie": return NYStyleVeggiePizza()
        if kind.lower() == "pepperoni": return NYStylePepperoniPizza()
        raise ValueError(f"No NY pizza for kind: {kind}")

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        if kind.lower() == "cheese": return ChicagoStyleCheesePizza()
        if kind.lower() == "veggie": return ChicagoStyleVeggiePizza()
        if kind.lower() == "pepperoni": return ChicagoStylePepperoniPizza()
        raise ValueError(f"No Chicago pizza for kind: {kind}")
