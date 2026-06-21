daily_sales = [1200, 3400, 2100, 4500, 1800, 5200, 2900]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day, sale in zip(days, daily_sales):
    print(f"{day}: Rs.{sale}")
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
print(f"Total Sales: Rs.{total_sales}")
print(f"Average Sales: Rs.{average_sales:.2f}")
highest_sale = max(daily_sales)
highest_day = daily_sales.index(highest_sale)
print(f"Highest Sale: Rs.{highest_sale} on {days[highest_day]}")
lowest_sale = min(daily_sales)
lowest_day = daily_sales.index(lowest_sale)
print(f"Lowest Sale: Rs.{lowest_sale} on {days[lowest_day]}")
count = 0
for sale in daily_sales:
    if sale > average_sales:
        count += 1
print(f"Days above average sales: {count}")
count = 0
for sale in daily_sales:
    if sale < 2000:
        count += 1
print(f"Days with low sales: {count}") 
departments = ["Sales", "Analytics", "Engineering"]
employees =   [4, 6, 8]
# For each department, print the department name and then print "Employee [n]" for each employee in that department.
for department in departments:
    print(f"{department}: ")

