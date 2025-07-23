
cart = []

def add_item(item):
    cart.append(item)
    print(f"Added '{item}' to the cart.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"Removed '{item}' from the cart.")
    else:
        print(f"'{item}' not found in the cart.")

def remove_last_item():
    if cart:
        removed = cart.pop()
        print(f"Removed last added item: '{removed}'")
    else:
        print("Cart is already empty.")

def display_sorted_items():
    if cart:
        print("Items in alphabetical order:")
        for item in sorted(cart):
            print(f"- {item}")
    else:
        print("Cart is empty.")

def display_cart():
    if cart:
        print("Current Cart:")
        for idx, item in enumerate(cart):
            print(f"{idx}: {item}")
    else:
        print("Cart is empty.")

print("Shopping Cart Initialized")

add_item("apples")
add_item("bread")
add_item("milk")
add_item("eggs")

remove_item("bread")

remove_last_item()

display_sorted_items()

display_cart()
