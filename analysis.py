def spending_analysis(transactions):
    total_expense=0
    category_totals={}
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

    highest_category = ""
    highest_amount = 0

    for ct in category_totals:
        if category_totals[ct] > highest_amount:
            highest_amount = category_totals[ct]
            highest_category = ct

    if highest_category != "":
        print("Highest Spending Category:", highest_category, "-", highest_amount)

    else:
        print("No expenses recorded")
