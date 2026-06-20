name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
existing_loans = input("Do you have any existing loans? (yes/no): ").lower()
if age < 21:
    print(f"Sorry {name}, you are too young to apply")
elif income < 15000:
    print(f"Sorry {name}, minimum income requirement is Rs.15000")
elif credit_score < 600:
    print(f"Sorry {name}, credit score is too low. Minimum is 600")
elif existing_loans == "yes":
    print(f"Sorry {name}, please clear existing loans before applying")
else:
    print(f"Congratulations {name}! You are eligible. Your application is under review.")