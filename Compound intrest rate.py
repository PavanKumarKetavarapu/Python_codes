principle_amount=float(input("enter deposited money "))
time_period=float(input("enter the time period in years "))
intrest_rate=float(input("enter the intrest rate per year "))
compound_intresrt=principle_amount*(1+(intrest_rate/100))**time_period
print("total amount to be saved",compound_intresrt)