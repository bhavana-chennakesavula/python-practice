# Start with this inventory
inventory = {
    "Rice": {"price": 60, "stock": 500, "category": "Food"},
    "Dal": {"price": 120, "stock": 200, "category": "Food"},
    "Shampoo": {"price": 180, "stock": 80, "category": "Personal Care"},
    "Oil": {"price": 150, "stock": 120, "category": "Food"},
    "Soap": {"price": 40, "stock": 300, "category": "Personal Care"}
}
print(f"inventory: {inventory}")
print(f"price of dal: {inventory['Dal']['price']}")
print(f"stock of shampoo: {inventory['Shampoo']['stock']}")
inventory['Sugar'] = {"price": 50, "stock": 400, "category": "Food"}
inventory['Rice']['price'] = 75
print(f"Updated inventory: {inventory}")
del inventory['Soap']
print(f"Product name: {inventory.keys()}")
print(f"total no.of products: {len(inventory)}")
print(inventory.get('mobile','Not Available'))
print(f"{max(inventory)}")