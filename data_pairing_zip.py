# Given lists
products = ["laptop", "mouse", "keyboard", "monitor"]
prices = [800, 20, 50, 150]
quantities = [5, 50, 8, 12]

product_price_pairs = list(zip(products, prices))
print("Product-Price Pairs:")
for product, price in product_price_pairs:
    print(f"- {product.capitalize()}: ${price}")

print("\nTotal Inventory Value for Each Product:")
for product, price, quantity in zip(products, prices, quantities):
    total_value = price * quantity
    print(f"- {product.capitalize()}: ${total_value}")

catalog = {
    product: {"price": price, "quantity": quantity}
    for product, price, quantity in zip(products, prices, quantities)
}
print("\nProduct Catalog Dictionary:")
for name, data in catalog.items():
    print(f"- {name.capitalize()}: Price = ${data['price']}, Quantity = {data['quantity']}")

low_stock = [product for product, qty in zip(products, quantities) if qty < 10]
print("\nLow Stock Products (quantity < 10):")
for name in low_stock:
    print(f"- {name.capitalize()}")
