from store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    ny.order_pizza("cheese")
    chi.order_pizza("clam")

    
    ny.order_pizza("pepperoni")
    chi.order_pizza("Pepperoni")
    
    ny.order_pizza("veggie")
    chi.order_pizza("veggie")

if __name__ == "__main__":
    main()
