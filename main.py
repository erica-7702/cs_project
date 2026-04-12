from analysis import spending_analysis

def forecast(balance, months, monthly_income, monthly_expense):
    for i in range(months):
        balance += monthly_income - monthly_expense
    return balance

def Main():
    print("Welcome to Personal Finance System")

    name = input("Enter your name: ")

    while True:
        try:
            balance = float(input("Enter your starting balance: "))
            break
        except:
            print("Invalid Input. Please enter a number")

    transactions = []
    income_type = ["salary", "allowance", "business", "other"]
    categories = ["food", "rent", "transport", "clothes", "miscellaneous"]
    limits = {}

    print("Set your budget limits")

    for category in categories:
        try:
            amount = float(input(f"Enter limit for {category}: "))
        except:
            print("Invalid input, setting default 0")
            amount = 0

        limits[category] = amount

    print("Profile created successfully for", name)
    while True:
        print("\n PERSONAL FINANCE SYSTEM")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Filter transactions")
        print("6. Forecast Future Balance")
        print("7. Save data")
        print("8. Load data")
        print("9. Spending Analysis")
        print("10. Exit")

        choice = input('Enter option (1-10):')
        if choice == "1":
            try:
                amount = float(input('Enter income amount:'))
            except:
                print("Invalid!, Enter a number")
                continue

            print("Income categories:", income_type)
            income_type = input('Enter income type: ').strip().lower()

            if income_type not in income_type:
                print("Invalid category")
                continue
            balance = balance + amount
            transactions.append(("Income", amount, income_type))

        elif choice == '2':
            try:
                amount = float(input('Enter expenses amount:'))
            except:
                print("Invalid!, Enter a number")
                continue

            print("Expense categories:", categories)
            category = input('Enter expense category: ').strip().lower()

            if category not in categories:
                print("Invalid category! Choose from:", categories)
                continue
            balance -= amount
            transactions.append(("Expense", amount, category))

            if category in limits:
                total = 0

                for t in transactions:
                    if t[0] == "Expense" and t[2] == category:
                        total += t[1]

                if total > limits[category]:
                    print("Warning: You have exceeded your budget for", category)

        elif choice == '3':
            print(name, "'s Current Balance", balance)

        elif choice == '4':
            if len(transactions) == 0:
                print("** no transactions recorded; make a transaction to view this data **")

            else:
                print("\n--- Transactions ---")
                for t in transactions:
                    print(f"{t[0]} | Amount: {t[1]} | Category: {t[2]}")

        elif choice == '5':
            category = input("Enter category to filter: ").strip().lower()

            found = False
            for t in transactions:
                if t[0] == "Expense" and t[2] == category:
                    print(f"{t[0]} | {t[1]} | {t[2]}")
                    found = True

            if not found:
                print("No transactions found for this category")

        elif choice == '6':
            try:
                months = int(input("Enter the number of months: "))
            except:
                print("Invalid input")
                continue

            try:
                monthly_income = float(input("Enter expected monthly income: "))
            except:
                print("Invalid input, assumed monthly income is 0")
                monthly_income = 0

            try:
                monthly_expense = float(input("Enter expected monthly expense: "))
            except:
                print("Invalid input, assumed monthly expense is 0")
                monthly_expense = 0

            future = forecast(balance, months, monthly_income, monthly_expense)
            print('Estimated future balance after', months, 'months:', future)

        elif choice == '7':
            with open('finance_data.txt', 'w') as file:
                for t in transactions:
                    file.write(f"{t[0]},{t[1]},{t[2]}\n")

                print('Data successfully saved')

        elif choice == '8':
            balance = 0.0
            transactions = []
            try:
                with open('finance_data.txt', 'r') as file:
                    for line in file:
                        data = line.strip().split(",")
                        t_type = data[0].strip()
                        amount = float(data[1].strip())
                        category = data[2].strip()
                        transactions.append((t_type, amount, category))

                        if t_type == "Income":
                            balance += amount
                        else:
                            balance -= amount

                print("Data successfully loaded")
            except:
                print("No saved file")

        elif choice == '9':
            if len(transactions) == 0:
                print("No data to analyse.")
            else:
                spending_analysis(transactions)

        elif choice == '10':
            print("Exiting. Goodbye")
            break

        else:  
            print('Invalid Input')

Main()