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
    categories = ["food", "rent", "transport", "clothes", "miscellaneous"]
    limits = {}

    print("Set your budget limits:")

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
        print("5. Forecast Future Balance")
        print("6. Save data")
        print("7. Load data")
        print("8. Spending Analysis")
        print("9. Exit")

        choice = input('Enter choice:')
        if choice == "1":
            try:
                amount = float(input('Enter income amount:'))
            except:
                print("Invalid!, Enter a number")
                continue
            category = input('Enter Category (salary, allowance):')
            balance = balance + amount
            transactions.append(("Income", amount, category))

        elif choice == '2':
            try:
                amount=float(input('Enter expenses amount:'))
            except:
                print("Invalid!, Enter a number")
                continue


            print("Categories:", categories)
            category=input('Enter category:').strip().lower()
            if category not in categories:
                print("Invalid category!, Choose from:",categories)
                continue
            balance-=amount
            transactions.append(("Expense", amount,category))

            if category in limits:
                total = 0

                for t in transactions:
                    if t[0] == "Expense" and t[2] == category:
                        total += t[1]

                if total > limits[category]:
                    print("Warning: You have exceeded your budget for", category)


        elif choice == '3':
            print(name, "'s Current Balance", balance)

        elif choice == "4":
            for t in transactions:
                print("Type:", t[0])
                print("Amount:", t[1])
                print('Category:', t[2])

        elif choice == '5':
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
            print('Estimated future balance: ', future)

        elif choice == '6':
            with open('finance_data.txt', 'w') as file:
                for t in transactions:
                    line = t[0] + ', ' + str(t[1]) + ', ' + t[2]+ "\n"
                    file.write(line)

                print('Data successfully saved')

        elif choice == '7':
            balance = 0.0
            transactions = []
            try:
                with open('finance_data.txt', 'r') as file:
                    for line in file:
                        data = line.strip().split(",")
                        t_type = data[0]
                        amount = float(data[1])
                        category = data[2]
                        transactions.append((t_type, amount, category))

                        if t_type == "Income":
                            balance += amount
                        else:
                            balance -= amount

                print("Data successfully loaded")
            except:
                print("No saved file")

        elif choice == '8':
            spending_analysis(transactions)
        elif choice == '9':
            print("Exiting. Goodbye")
            break

        else:
            print('Invalid Input')

Main()