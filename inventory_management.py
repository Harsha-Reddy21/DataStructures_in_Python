inventory = {
    "apples": {"price": 1.5, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.0, "quantity": 80}
}

inventory["pears"] = {"price": 2.3, "quantity": 90}
print("Added new product: pears")

inventory["bananas"]["price"] = 2.0
print("Updated price of bananas to $2.0")

if inventory["apples"]["quantity"] >= 25:
    inventory["apples"]["quantity"] -= 25
    print("Sold 25 apples")
else:
    print("Not enough apples in stock")

total_value = sum(info["price"] * info["quantity"] for info in inventory.values())
print(f"\nTotal Inventory Value: ${total_value:.2f}")

low_stock = {name: info for name, info in inventory.items() if info["quantity"] < 100}
print("\nLow Stock Products (quantity < 100):")
for name, info in low_stock.items():
    print(f"- {name.capitalize()}: {info['quantity']} units")
