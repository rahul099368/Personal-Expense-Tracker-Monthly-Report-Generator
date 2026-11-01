import random 
import datetime as dt

from tabulate import tabulate

import expense_utils as eu
import report_utils as ru
#main implementation
def main():
    print("----EXPENSE TRACKER----")
    expenses = []
    reference_ids = []
    num = int(input("How many expenses are there: "))
    for i in range(num):
        print("\nenter details of expense",1+i)
        description = input("Enter description: ")
        category = input("Enter category: ")
        amount = float(input("Enter Amount : (RS)"))
        if eu.validate_expense(amount) == False:
           amount = float(input("invalid amount, enter valid amount: "))
        date = input("Enter date (YYYY-MM-DD), blank for today): ")
        if date == "":
           date  = dt.date.today().strftime("%Y-%m-%d")
        num_part = random.randint(100000,999999)
        while True:
            ref_id = "EXP-"+str(num_part)
            if ref_id not in reference_ids:
                reference_ids.append(ref_id)
                break
        print(f"Reference ID: {ref_id}")
        expense={
            "description":description,
            "category":category,
            "amount":amount,
            "date":date,
            "reference id":ref_id
            }
        expenses.append(expense)
        print("expense recorded successfully...")
    #
    report = ru.generate_report(expenses)
    monthly_expense = report['expenses']
    #create table 
    print("\n\n-----MONTHLY EXPENSE REPORT-----\n")
    table_data=[]
    for expense in monthly_expense:
        table_data.append([
            expense['reference id'],
            expense['date'],
            expense['description'],
            expense['category'],
            f"{expense['amount']:.2f}"
        ])
    headers=[
        'Reference ID',
        'Date',
        'Description',
        'category',
        'Amount'
    ]
    print(tabulate(table_data,headers=headers))

    #to print total spending 
    print("\nTotal spending:",report['total'])
    #to print average spending
    print("Average spending:",report['average'])

    #category wise spending
    print("\nCategory wise spending: ")
    for category,amount in report['category total'].items():
        print(f"{category}: RS.{amount}")

    #to get current month(%B) is for to find the full name of month  
    current_month = dt.date(report['year'],report['month'],1).strftime("%B")
    print("\nReport month:",current_month,report['year'])

if __name__ == "__main__":
    main()