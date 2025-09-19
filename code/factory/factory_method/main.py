from store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1)
    p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2)
    
    p3 = ny.order_pizza("veggie"); print("Ethan ordered:", p3)
    p4 = chi.order_pizza("veggie"); print("Joel ordered:", p4)
    
    p5 = ny.order_pizza("pepperoni"); print("Ethan ordered:", p5)
    p6 = chi.order_pizza("pepperoni"); print("Joel ordered:", p6)

if __name__ == "__main__":
    main()
