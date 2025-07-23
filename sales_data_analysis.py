
sales_data = [
    [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)],  # Q1
    [("Apr", 1300), ("May", 1250), ("Jun", 1400)],  # Q2
    [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)]   # Q3
]

print("Total Sales per Quarter:")
for idx, quarter in enumerate(sales_data, start=1):
    total = sum(sale for _, sale in quarter)
    print(f"Q{idx}: ${total}")

highest_month = ("", 0)
for quarter in sales_data:
    for month, sale in quarter:
        if sale > highest_month[1]:
            highest_month = (month, sale)

print(f"\nHighest Sales Month: {highest_month[0]} with ${highest_month[1]}")

flat_sales = [(month, sale) for quarter in sales_data for (month, sale) in quarter]
print("\nFlat List of Monthly Sales:")
print(flat_sales)

print("\nDetailed Monthly Sales with Quarters:")
for q_num, quarter in enumerate(sales_data, start=1):
    for month, sale in quarter:
        print(f"Quarter {q_num} - {month}: ${sale}")
