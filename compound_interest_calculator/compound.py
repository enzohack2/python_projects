# import math module
import math as m

# compound interest function 
def cInterest(p, r, n, t):
    """
    Function that calculates compound interest.
    Inputs: principal, interest rate, copmound interval as n and duration of investment in years as t"""
    
    calc = p * m.pow((1 + r/n), n*t )
    return calc

# user input
principal = float(input("Principal: £"))
interestRate = float(input("Interest rate as a decimal (2% = 0.02): "))
compoundInterval = int(input("Copmound interval (2 = semi anually, 365 = daily): "))
duration = int(input("Investment duration in years: "))

# output results
result = round(cInterest(principal, interestRate, compoundInterval, duration), 2) # rounded to 2 decimal places for simplicity ;)
print("Total compounded amount = £{}".format(result))

# Thanks for watching :)