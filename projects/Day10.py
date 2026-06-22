expenses = []
expenses_amount = []
while True:
    print(" === EXPENSE TRACKER === ")
    expense_list = ['Add expense', 'View total', 'View all expenses', 'Quit']
    for i,expense in enumerate(expense_list, 1):
        print(f"{i}. {expense}")
    try:
        choice = int(input("enter your choice:"))
    except ValueError:
        print("Please enter serial number of the choice from the above list")
        continue
    if choice == 1:
        new_expense = input("enter your new expense: ")
        try:
            new_amount = int(input("enter the amount of the expense: "))
        except ValueError:
            print("please enter the amount in digits")
            continue
        expenses.append(new_expense)
        expenses_amount.append(new_amount)
    elif choice == 2:
        print(f"total of all your expenses is: {sum(expenses_amount)}")
    elif choice == 3:
        print("your expenses: ")
        for expensee, amount in zip(expenses, expenses_amount):
            print(f"{expensee}: {amount}")
    elif choice == 4:
        break
    else:
        print("Invalid input! Please try again later")
