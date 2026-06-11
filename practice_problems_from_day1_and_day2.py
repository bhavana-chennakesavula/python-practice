# Problem 1: Ask a user for their monthly salary. Calculate and print how much they earn in a year.

salary_per_month = int(input("enter your monthly salary: "))
salary_per_year = salary_per_month * 12
print(f" you earn {salary_per_year} per year.")



# Problem 2: Ask for the length and width of a rectangle. Calculate and print the area.

length = int(input("enter length of a rectangle: "))
breadth = int(input("enter breadth of a rectangle: "))
area = length * breadth
print(f"area of rectangle is {area}")



# Problem 3: Ask a user for an amount in USD. Convert it to INR  and print the result.

amount_in_usd = int(input("enter amount in usd: "))
rupees = amount_in_usd*83
print(f"${amount_in_usd} are {rupees} in rupees")



# Problem 4: Ask a user for a price and a quantity. Calculate the total cost and print it.

price = input("enter price of the item: ")
quantity = int(input("enter no.of items you bought: "))
cost = float(price)
total_cost = cost*quantity
print(f'your total is {total_cost:.2f}.')



# Problem 5: Ask for a temperature in Celsius. Convert to Fahrenheit using the formula: F = (C × 9/5) + 32. Print the result with 1 decimal place using f-string.

Celcius = input("enter temparature in celsius: ")
c = float(Celcius)
F = (c * 9/5) + 32
print(f'{c}degree celcius is {F:.1} fahrenhieat')



# Problem 6: Ask a user for their first name and last name. Print: "Your full name is [first] [last]" using an f-string.

first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
print(f'your name is {first_name} {last_name}')



# Problem 7: Ask a user for their name and age. If they're 18 or older, print "You are an adult, [name]". If younger, print "You are a minor, [name]".

name = input("enter your name: ")
age = int(input("enter your name: "))
if age>= 18:
    print(f'you are an adult, {name}')
else:
    print(f'you are a minor, {name}')