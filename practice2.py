"""
-------------------------------------------------------------------------------
Name:		practice2.py
Purpose: To determine if fees need to be paid at customs when reentering Canada based on the monetary value of goods purchased during time spent abroad

Author:	Au.E

Created:	01/06/2021
-------------------------------------------------------------------------------
"""

total = 0
days_count = 0
done = False

while not done:
  daily_amount = float(input("Enter a daily spent amount (-1 to stop): "))

  if daily_amount == -1:
    done = True
  else:
    total = total + daily_amount
    days_count = days_count + 1

# output number of days and total spent
print("Total days travelled: " + str(days_count))
print("Total amount spent: $" + str(total))

# check if they've gone over the limit
limit = 250 * days_count
if total > limit:
  fee = total * 0.13
  print("You owe a fee of $" + str(round(fee, 2)))
else:
  print("You do not owe a fee!!!")

