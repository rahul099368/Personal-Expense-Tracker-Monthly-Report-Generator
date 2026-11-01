import datetime as dt
import expense_utils as eu
#to get current month
def get_current_month():
    today = dt.date.today()
    month = today.month
    year = today.year
    return month,year

#to filter monthly expenses
def filter_monthly_expense(expenses,month,year):
    monthly_expenses = []
    for expense in expenses:
        expense_date = dt.datetime.strptime(expense['date'],"%Y-%m-%d")
        if expense_date.month == month and expense_date.year == year:
            monthly_expenses.append(expense)
    return monthly_expenses

#to generate final report
def generate_report(expenses):
    month,year = get_current_month()
    monthly_expense = filter_monthly_expense(expenses,month,year)
    total = eu.calculate_total(monthly_expense)
    average = eu.calculate_average(monthly_expense)
    category_total = eu.category_summary(monthly_expense)
    report = {
        "month":month,
        "year":year,
        "expenses":monthly_expense,
        "total":total,
        "average":average,
        "category total":category_total
    }
    return report
