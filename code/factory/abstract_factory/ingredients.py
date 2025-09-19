from abc import ABC, abstractmethod

# Ingredient products
class Dough:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Sauce:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Cheese:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Clams:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Pepperoni:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Veggies:
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
    @abstractmethod
    def create_veggies(self) -> Veggies: ...
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")
    def create_veggies(self) -> Veggies: return Veggies("Garlic, Onion, Mushroom, Red Pepper")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Sliced Pepperoni")
    

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")
    def create_veggies(self) -> Veggies: return Veggies("Garlic, Tomato")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Diced Pepperoni")
  
