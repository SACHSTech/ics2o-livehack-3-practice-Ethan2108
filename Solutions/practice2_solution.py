"""
-------------------------------------------------------------------------------
Name:		practice2.py
Purpose:	livehack3 practice question

Author:	 Fabroa.E

Created:	01/05/2021
-------------------------------------------------------------------------------
"""

total = 0
days_count = 0
done = False

while not done:
  daily_amt = float(input("Enter a daily spent amount (-1 to stop): "))

  if daily_amt == -1:
    done = True
  else:
    total = total + daily_amt
    days_count = days_count + 1

# output number of days and total spent
print("Total days travelled: " + str(days_count))
print("Total amount spent: $" + str(total))

# check if they've gone over the limit
limit = 250 * days_count
if total > limit:
  fee = total * 0.13
  print("You owe a fee of $" + str(round(fee,2)))
else:
  print("Phew, you do not owe a fee.")


