"""
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	livehack3 practice question

Author:	 Fabroa.E

Created:	01/05/2021
-------------------------------------------------------------------------------
"""

"""
Enter the Canadian to US Dollar exhange rate: 0.75
Enter the starting value: 10
Enter the end value: 200
"""

# get the exchange rate and start and end of table
exchange_rate = float(input("Enter the Canadian to US Dollar exhange rate: "))
start_value  = int(input("Enter the starting value: "))
end_value  = int(input("Enter the end value: "))

# table header
print("Can Price  --> US Price")

# output table
for cdn_amount in range (start_value, end_value+1, 10):
  usd_amount = cdn_amount * exchange_rate
  print(str(cdn_amount) + " --> " + str(usd_amount))