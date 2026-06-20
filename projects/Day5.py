last_month = {"Ravi", "Priya", "Arjun", "Sneha", "Kiran"}
this_month = {"Priya", "Arjun", "Kiran", "Meera", "Bhavana"}
categories = ("Electronics", "Clothing", "Food", "Books", "Sports")
print(f"Total unique customers across both months: {last_month | this_month}")
print(f"Customers who came back this month: {last_month & this_month}")
print(f"Customers lost this month: {last_month - this_month}")
print(f"New customers this month: {this_month - last_month}")
print(f"Total number of product categories: {len(categories)}")
print(f"first category: {categories[0]}. Last category: {categories[-1]}")
gadgets, clothes, food = categories[:3]
print(gadgets, clothes, food)
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")
print(f"First month: {months[0]}")
print(f"Last month: {months[-1]}")
print(f"Total months: {len(months)}")
week1 = {"rice", "dal", "oil", "sugar", "salt"}
week2 = {"dal", "sugar", "milk", "bread", "oil"}
print(f"products that appear in both weeks: {week1 & week2}")
customer_ids = [101, 202, 303, 101, 404, 202, 505]
unique = set(customer_ids)
print(f"No.of duplicates: {len(customer_ids) - len(unique)}")