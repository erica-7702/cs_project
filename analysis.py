def spending_analysis(transactions):
    total_expense = 0
    category_totals = {}
    for t in transactions:
        if t[0] == "Expense":
            amount = t[1]
            category = t[2]

            total_expense += amount

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    print("\n~ Spending Analysis ~")
    print("Total Expenses:", total_expense)

    print("\nSpending by Category:")
    for cat in category_totals:
        print(cat, ":", category_totals[cat])

    highest_category = ""
    highest_amount = 0

    for ct in category_totals:
        if category_totals[ct] > highest_amount:
            highest_amount = category_totals[ct]
            highest_category = ct

    if highest_category != "":
        print("Highest Spending Category:", highest_category, "-", highest_amount)

        print("\nAverage Spending per Category:")
        for cat in category_totals:
            count = 0
            total = 0

            for t in transactions:
                if t[0] == "Expense" and t[2] == cat:
                    total += t[1]
                    count += 1

            if count > 0:
                average = total / count
                print(cat, "average spending:", average)

    else:
        print("No expenses recorded")
