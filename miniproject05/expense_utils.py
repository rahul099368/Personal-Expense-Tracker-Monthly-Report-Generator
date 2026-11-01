#to validate expenses
def validate_expense(exp_amount):
    if exp_amount >= 0:
        return True
    else:
        return False

#to calculate total spending
def calculate_total(expenses):
    total_spend = 0
    for expense in expenses:
        total_spend += expense['amount']
    return total_spend

#to calculate average of expenses
def calculate_average(expenses):
    if len(expenses) == 0:
        return 0
    average = calculate_total(expenses)/len(expenses)
    return average

#to find category wise total
def category_summary(expenses):
    category_total = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount
    return category_total


