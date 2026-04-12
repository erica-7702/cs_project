def save_data(transactions):
    with open('finance_data.txt', 'w') as file:
        for t in transactions:
            file.write(f"{t[0]},{t[1]},{t[2]}\n")

    print("Data successfully saved")


def load_data():
    transactions = []
    balance = 0.0

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

    return transactions, balance