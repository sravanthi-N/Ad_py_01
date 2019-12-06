def make_pizza(size,*toppings):
    """ Summarise the pizza details that we are about to make.."""
    print(f"\n Making a {size}-inch piza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")


make_pizza(12, 'cheese', 'jalapinoes', 'olive')
