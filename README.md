# ICS2O LiveHack #3 Practice


## Practice #1

The mega Canadian clothing store chain, Forever Fab, has noticed an increase in the number 
of American customers over the past year due to the widening difference between the Canadian 
and U.S dollars.  Forever Fab lists its prices in Canadian dollars and American customers 
frequently complain about the "high prices", not realizing that with the currency exchange, 
they are getting a discount.   The store has taken the initiative to educate its American 
customers by displaying currency conversion tables throughout their stores.

Create an program that takes in the Canadian to U.S dollar exchange rate, starting price, and ending price, and then outputs a conversion table of Canadian to U.S Dollars with increments of $10

```
Enter the Canadian to US Dollar exhange rate: 0.75
Enter the starting value: 10
Enter the end value: 200

Can Price  --> US Price
10 --> 7.5
20 --> 15
30 --> 22.5
...
200 --> 150.0
```

## Practice #2

You have been away traveling in the U.S and now you are ready to return home.  You’ve done a lot of shopping and are worried about paying duty fees when you enter back into Canada.  Canada Customs allows **$250 worth of purchased goods for each day abroad**.  A fee of **13%** of the total value of purchased goods must be paid if the total value is greater than the allowable amount.   For example, if you travel for 7 days and you purchase a total of $1,946, a fee of $252.98 must be paid (since the limit for travelling 7 days is $250x7days= $1750)

Write a program that allows you to enter the amount spent for each day of your trip, stopping once you enter -1.  Output the total days travelled and the total amount spent.  If a fee is owed based on the total amount spent and the number of days travelled output the fee.  Otherwise output “Phew, you do not have to pay a fee”.

### Sample Run 1:
```
Enter a daily spent amount (-1 to stop): 200
Enter a daily spent amount (-1 to stop): 303
Enter a daily spent amount (-1 to stop): 276
Enter a daily spent amount (-1 to stop): 309
Enter a daily spent amount (-1 to stop): -1
Total Days travelled: 4
Total amount spent: $1088.0
You owe a fee of $141.44
```

### Sample Run 2:
```
Enter a daily spent amount (-1 to stop): 176  
Enter a daily spent amount (-1 to stop): 255  
Enter a daily spent amount (-1 to stop): 320  
Enter a daily spent amount (-1 to stop): 45  
Enter a daily spent amount (-1 to stop): 200  
Enter a daily spent amount (-1 to stop): -1  
Total Days travelled: 5  
Total amount spent: $996.0  
Phew, you do not owe a fee  
```


