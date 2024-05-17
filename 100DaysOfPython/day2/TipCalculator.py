from decimal import *

def CalculateBillPerPerson(bill, tipPercentage, split):
    totalBill = float(bill) + (float(bill) * (int(tipPercentage)/100))

    return Decimal(str(totalBill/int(split))).quantize(Decimal('.01'), rounding=ROUND_UP)

if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    bill = input("What was the total bill? $")
    tipPercentage = input("How much tip would you like to give? 10, 12, or 15? ")
    split = input("How many people to split the bill? ")
    print("Each person should pay: ", CalculateBillPerPerson(bill, tipPercentage, split))