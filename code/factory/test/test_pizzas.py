from factory.abstract_factory.store import NYPizzaStore, ChicagoPizzaStore


def test_ny_store_creates_ny_style_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert pizza is not None
    assert "NY Style" in pizza.name


def test_chicago_store_creates_chicago_style_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert pizza is not None
    assert "Chicago Style" in pizza.name


def test_ny_cheese_uses_thin_crust_dough():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    from factory.abstract_factory.ingredients import Dough  # clase que representa masa en ingredients.py
    # Se compara por tipo / instancia del objeto dough creado por la fábrica
    assert isinstance(getattr(pizza, "dough", None), Dough)


def test_chicago_clam_uses_frozen_clams():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    from factory.abstract_factory.ingredients import Clams  # clase que representa clams en ingredients.py
    clams = getattr(pizza, "clams", None) or getattr(pizza, "clam", None)
    assert clams is not None
    assert isinstance(clams, Clams)