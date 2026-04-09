from analysis import spending_analysis

def forecast(balance,months,saving):
    if months==0:
        return balance
    return forecast(balance+saving,months-1,saving)

def Main():
    print("Welcome to Personal Finance System")
    name=input("Enter your name:")
    while True:
        try:
            balance=float(input("Enter your starting balance:"))
            break
        except:
            print("Invalid Input. Please enter a number")
    
    transactions=[]
    print("Profile created successfully for", name)
    limits = {
        "food": 2000,
        "rent": 4000,
        "transport": 600,
        "clothes": 400,
        "miscellaneous": 700
    }

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

        choice=input('Enter choice:')
        if choice=="1":
            try:
                amount=float(input('Enter income amount:'))
            except:
                print("Invalid!, Enter a number")
                continue
            category=input('Enter Category (salary,allowance):')
            balance= balance+amount
            transactions.append(("Income", amount,category))

        elif choice=='2':
            try:
                amount=float(input('Enter expenses amount:'))
            except:
                print("Invalid!, Enter a number")
                continue
            balance=balance-amount
            category=input('Enter category(food,rent,transport):')
            transactions.append(("Expense", amount,category))

            if category in limits:
                total = 0

                for t in transactions:
                    if t[0] == "Expense" and t[2] == category:
                        total += t[1]

                if total > limits[category]:
                    print("Warning: You have exceeded your budget for", category)

        elif choice=='3':
            print(name, "'s Current Balance",balance)

        elif choice=="4":
            for t in transactions:
                print("Type:",t[0])
                print("Amount:",t[1])
                print('Category:',t[2])

        elif choice=='5':
            try:
                months=int(input("Enter the number of months:"))
            except:
                print("Invalid Output")
                continue
            saving_input=input("Enter monthly savings:")
            if saving_input == "":
                saving=100
            else:
                try:
                    saving=float(saving_input)
                except:
                    print("Invalid input, using default 100")
                    saving=100

            future= forecast(balance,months,saving)
            print('Estimated future balance:',future)

        elif choice=='6':
            file=open('finance_data.txt','w')
            for t in transactions:
                line=t[0]+','+ str(t[1])+','+t[2]+"\n"
                file.write(line)
            file.close()
            print('Data successfully saved')

        elif choice=='7':
            balance=0.0
            transactions=[]
            try:
                file=open('finance_data.txt','r')
                for line in file:
                    data= line.strip().split(",")
                    t_type= data[0]
                    amount= float(data[1])
                    category= data[2]
                    transactions.append((t_type,amount,category))

                    if t_type=="Income":
                        balance+=amount
                    else:
                        balance-=amount
                file.close()
                print("Data successfully loaded")
            except:
                print("No saved file")

        elif choice=='8':
            spending_analysis(transactions)
        elif choice=='9':
            print("Exiting. Goodbye")
            break

        else:
            print('Invalid Input')

Main()
