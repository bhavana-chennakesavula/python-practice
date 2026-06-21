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
    
    
# Problem 8: You received "         bhavana CHENNAKESAVULa          " from a form: Clean it and print: first name, last name, full name in title case, and total characters in full name (without spaces).
    
name = "         bhavana CHENNAKESAVULa          "
full_name = name.strip()
clean_name = full_name.split()
print(clean_name[0])
print(clean_name[1])
print(full_name.title())
print(len(full_name))



# Problem 9: A product price came in as "INR 2,500.00". Extract just the number, remove the comma, convert to float, apply 18% GST and print the final price with 2 decimal places.

cost = "INR2,500.00"
price = cost[3: ]
clean_price = price.replace(",","")
pprice = float(clean_price)
price_after_GST = pprice * 1.18
print(f"{price_after_GST:.2f}")



# Problem 10: You have this string: "2026-06-10". Extract and print: Year, Month, Day Using slicing only. No split().

date = "2026-06-10"
print("year: "+ date[0:4])
print("month: "+ date[5:7])
print("Date: "+ date[8: ])



# Problem 11: You received a CSV row as a string: "Bhavana,23,Ongole,Data Analyst". Split it and print each value on a separate line with a label like: Name: Bhavana   Age: 23     City: Ongole    Role: Data Analyst

string = "Bhavana,23,Ongole,Data Analyst"
final_string = string.split(",")
print("Name: "+ final_string[0])
print("Age: "+ final_string[1])
print("City: "+ final_string[2])
print("Role: "+ final_string[3])



# Problem 12: Ask the user to enter a sentence. Print: The sentence in uppercase, Total number of characters, The sentence with all spaces removed, The first 10 characters only

sentence = input("enter a sentence: ")
print(sentence.upper())
print(len(sentence))
print(sentence.replace(" ", ""))
print(sentence[0:11])
