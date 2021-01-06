"""
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose: To create a program that takes in the starting price, and ending price based on the Canadian to U.S dollar exchange rate, and then outputs a conversion table of Canadian to U.S Dollars with increments of $10.

Author:	 Au.E

Created:	01/06/2021
-------------------------------------------------------------------------------
"""


# get the exchange rate and start and end of table
exchange_rate = 0.75
start_value  = int(input("Enter the starting value: "))
end_value  = int(input("Enter the end value: "))

# table header
print("Can Price  --> US Price")

# output table
for cdn_amount in range (start_value, end_value+1, 10):
  usd_amount = cdn_amount * exchange_rate
  print(str(cdn_amount) + " --> " + str(usd_amount))
