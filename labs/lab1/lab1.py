"""
Name: <Ashlyn Whittemore>
<lab1.py>

Problem: <How to use simple Python programming arithmatic to solve problems related to credit cards.
(avg. daily balance, monthly interest>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Professor Ashley Woods>
"""

def monthly_interest():
    annual_interest = eval(input("Enter the annual interest rate: (%) "))

# Read Number of Days
    num_days = int(input("Enter the number of days in the billing cycle: "))

# Previous Balance
    previous_bal = float(input("Enter the previous balance: "))

# Payment Amount
    payment_amt = float(input("Enter the payment amount: "))

# The day that the payment was made
    payment_day = eval(input("Enter the day that the payment was made in the billing cycle: "))


# Getting the Avg Daily Balance

    step1 = previous_bal*num_days
    step2 = payment_amt*(num_days-payment_day)
    step3 = step1-step2
    avg_daily_bal = step3/num_days

# Calculating and Output of Monthly Interest Charge

    monthly_rate = annual_interest/(12.0*100) # calculate Monthly Interest Rate
    monthly_interest = avg_daily_bal*monthly_rate # Getting the net balance

    print(monthly_interest)

monthly_interest()