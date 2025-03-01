## Conditional-Statements-Advanced

# Conditional Statements Advanced - Lab

### Tasks:

01. Day of Week:

   Write a program that reads an integer entered by the user and prints the day of the week, in the range [1...7], or prints "Error" in case the entered number is invalid.

  ########

02. Weekend or Working Day:

   Write a program that reads the day of the week (text), entered by the user. If the day is working, it prints on the console - "Working day", if it is a holiday - "Weekend". If a text other than a day of the week is entered, "Error" will be printed.

########

03. Animal Type:

Write a program that reads an integer from the console and on each successive line integers until their sum is greater than or equal to the original number. After reading is complete, print the sum of the entered numbers.

########

04. Personal Titles:

Write a program that reads a number n entered by the user and prints all numbers ≤ n from the sequence: 1, 3, 7, 15, 31, …. Each subsequent number is calculated by multiplying the previous one by 2 and adding 1.

########

05. Small Shop:

Write a program that calculates how much total money is in the account after you make a certain number of deposits. On each line you will receive the amount you need to deposit into the account until you receive a "NoMoreMoney" command. For each amount received, "Increase: " + the amount must be displayed on the console and added to the account. If you get a number less than 0 the console should display "Invalid operation!"  and the program to end. When the program ends, it should print "Total: " + the total amount in the account formatted to the second decimal place.

########

06. Number in Range:

Write a program that, until the "Stop" command is received, reads integers entered by the user, finds the largest among them, and prints it. Enter one number per line.

########

07. Working Hours:

Write a program that, until the "Stop" command is received, reads integers entered by the user, finds the smallest among them, and prints it. Enter one number per line.

########

08. Cinema Ticket:

Write a program that calculates the grade point average of a student over his entire course. On the first line, you will get the student's name, and on each subsequent line, their annual grades. The student advances to the next grade if his annual grade is greater than or equal to 4.00. If the student is interrupted more than once, the student is expelled and the program ends, printing the name of the student and the class in which he was expelled.

On successful completion of 12th grade to print:

"{student name} graduated. Average grade: {the average grade of the entire study}"

In case the student is excluded from school, print:

"{student name} has been excluded at {grade in which he was excluded} grade"

The value must be formatted to the second decimal place.


# Conditional Statements Advanced - Exercise

01. Cinema:

In a movie theater, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of screenings with tickets at different prices:
   
   • Premiere - premiere screening, at a price of BGN 12.00;
   
   • Normal - standard projection, at a price of BGN 7.50;
   
   • Discount - screening for children, schoolchildren and students at a reduced price of BGN 5.00.
    
Write a program that reads the projection type (text), number of rows and number of columns in the hall (integers) entered by the user and calculates the total ticket revenue for a full house. Print the result in 2 decimal places format.

########

02. Summer Outfit:

Summer is a season with very changeable weather and Victor needs your help. Write a program that, based on the time of day and the degrees, recommends Victor what clothes to wear. Your friend has different plans for each stage of the day, which also require a different appearance - you can see them from the table.
Exactly two lines are read from the console:

• Degrees - whole number;

• Time of day - text with three options "Morning", "Afternoon" or "Evening".

If 10 <= Degrees <= 18 -- Morning - Outfit = Sweatshirt and Shoes = Sneakers or -- Afternoon - Outfit = Shirt and Shoes = Moccasins or -- Evening - Outfit = Shirt and Shoes = Moccasins

If 18 < Degrees <= 24 -- Morning - Outfit = Shirt and Shoes = Moccasins or -- Afternoon - Outfit = T-Shirt and Shoes = Sandals or -- Evening - Outfit = Shirt and Shoes = Moccasins

If Degrees >= 25 -- Morning -Outfit = T-Shirt and Shoes = Sandals or -- Afternoon - Outfit = Swim Suit and Shoes = Barefoot or -- Evening - Outfit = Shirt and Shoes = Moccasins

As output, print to the console one line: "It's {degrees} degrees, get your {clothes} and {shoes}."

########

03. New House:
   
Marin and Nellie buy a house not far from Sofia. Nellie loves flowers so much that she convinces you to write a program to calculate how much it will cost them to plant a certain number of flowers and whether the available budget will be enough for them. Different flowers have different prices:

Rose = 5 

Dahlia = 3.80 

Tulip = 2.80 

Narcissus = 3 

Gladiola = 2.50

The following discounts are available:

· If Nellie buys more than 80 Roses - 10% discount from the final price;

· If Nellie buys more than 90 Dahlias - 15% discount from the final price;

· If Nellie buys more than 80 Tulips - 15% discount from the final price;

· If Nellie buys less than 120 Narcissus - the price increases by 15%;

· If Nelly Buys less than 80 Gladioli - the price increases by 20%.

3 lines are read from the console:

· Flower type - text with options "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus";

· Number of flowers - integer;

· Budget - integer

Output:

########

04. Fishing Boat:

Tony and his friends love to go fishing and are so passionate about fishing that they decide to go fishing by boat. The price for renting the boat depends on the season and the number of fishermen:

Depending on the season:

• The price for renting the boat in spring is 3000 BGN;

• The price for renting the boat in summer and autumn is 4200 BGN;

• The price for renting the boat in winter is 2600 BGN.

Depending on the number of the group, there is a different discount:

• If the group is up to 6 people inclusive - a 10% discount;

• If the group is from 7 to 11 people inclusive - a 15% discount;

• If the group is from 12 and up - a 25% discount.

Fishermen benefit from an additional 5% discount if they are an even number, unless it is autumn - then they do not have an additional discount, which is calculated after deducting the discount according to the above criteria.

Write a program that calculates whether the fishermen will collect enough money.

Input:

Three lines are read from the console:

• Budget of the group - an integer;

• Season - text: "Spring", "Summer", "Autumn" or "Winter";

• Number of fishermen - an integer.

Output:

The following is printed on the console:

• If the budget is sufficient:

"Yes! You have {the remaining money} leva left."

• If the budget IS NOT sufficient:

"Not enough money! You need {the amount that is not enough} leva."

· If their budget is sufficient - "Hey, you have a great garden with {number of flowers} {type of flowers} and {remaining amount} leva left.";

· If their budget is NOT enough - "Not enough money, you need {necessary amount} leva more.".

Amount to be formatted to the second decimal place. Amounts must be formatted to two decimal places.

########

05. Journey:

A young programmer has a certain budget and free time in a given season. Write a program that takes the budget and season as input and outputs where the programmer will vacation and how much he will spend.
The budget determines the destination, and the season determines how much of the budget he will spend. If it is summer, he will vacation at a campsite, and in winter at a hotel. If he is in Europe, regardless of the season, he will vacation at a hotel. Each campsite or hotel, depending on the destination, has its own price, which corresponds to a certain percentage of the budget:

• At 100 BGN or less - somewhere in Bulgaria:

◦ Summer - 30% of the budget;

◦ Winter - 70% of the budget.

• At 1000 BGN or less - somewhere in the Balkans:

◦ Summer - 40% of the budget;

◦ Winter - 80% of the budget.

• At more than 1000 BGN - somewhere in Europe:

◦ When traveling in Europe, regardless of the season, he will spend 90% of the budget.

Input:

The input is read from the console and consists of two lines entered by the user:

• Budget - a real number;

• One of the two possible seasons - "summer" or "winter".

Output:

Two lines should be printed to the console:

• "Somewhere in [destination]" between "Bulgaria", "Balkans" and "Europe"

• "{Holiday type} - {Amount spent}":

◦ The holiday can be between "Camp" and "Hotel"

◦ The amount should be formatted with accuracy to the second decimal place.

########

06. Operations Between Numbers:

Write a program that reads two integers (N1 and N2) and an operator to perform a given mathematical operation. The possible operations are: Addition(+), Subtraction(-), Multiplication(*), Division(/) and Modular Division(%.) When adding, subtracting and multiplying, the result and whether it is even or odd should be printed on the console. In the case of ordinary division - the result. In the case of modular division - the remainder. It should be borne in mind that the divisor can be equal to 0 (zero), and division by zero is not possible. In this case, a special message should be printed.

Input:

3 lines entered by the user are read from the console:

• N1 - integer;

• N2 - integer;

• Operator - one symbol from: "+", "-", "*", "/", "%".

Output:

Print one line to the console:

• If the operation is addition, subtraction, or multiplication:

◦ "{N1} {operator} {N2} = {result} - {even/odd}"

• If the operation is division:

◦ "{N1} / {N2} = {result}" - result, formatted to the second decimal place

• If the operation is modular division:

◦ "{N1} % {N2} = {remainder}"

• In case of division by 0 (zero):

◦ "Cannot divide {N1} by zero"

 ◦ „{N1} kann nicht durch Null geteilt werden“
 
Beispiele für Eingabe und Ausgabe

########

07. Hotel Room:

A hotel offers 2 types of rooms: studio and apartment. Write a program that calculates the price for the entire stay for a studio and an apartment. The prices depend on the month of stay:

May and October: Studio - 50 BGN/night; Apartment - 65 BGN/night

June and September: Studio - 75.20 BGN/night; Apartment - 68.70 BGN/night

July and August: Studio - 76 BGN/night; Apartment - 77 BGN/night

The following discounts are also offered:

• For a studio, for more than 7 nights in May and October: 5% discount.

• For a studio, for more than 14 nights in May and October: 30% discount.

• For a studio, for more than 14 nights in June and September: 20% discount.

• For an apartment, for more than 14 nights, regardless of the month: 10% discount.

Input:

The input is read from the console and contains exactly 2 lines entered by the user:

• On the first line is the month - May, June, July, August, September or October;

• On the second line is the number of nights - an integer.

Output:

To print 2 lines on the console:

• On the first line: "Apartment: {price for the entire stay} lv."

• On the second line: "Studio: {price for the entire stay} lv."

The price for the entire stay must be formatted with an accuracy of two decimal places.

########

08. On Time for the Exam:

A student must go to an exam at a certain time (for example, 9:30). He comes to the exam hall at a given arrival time (for example, 9:40). The student is considered to have arrived on time if he has arrived at the exam time or up to half an hour before. If he has arrived more than 30 minutes earlier, he is early. If he has arrived after the exam time, he is late. Write a program that reads the exam time and the arrival time and prints whether the student has arrived on time, whether he is early or late, and by how many hours or minutes he is early or late.

Input:

4 integers (one per line) entered by the user are read from the console:

• The first line contains the exam time - an integer from 0 to 23;

• The second line contains the exam minute - an integer from 0 to 59;

• The third line contains the arrival time - an integer from 0 to 23;

• The fourth line contains the minute of arrival - an integer from 0 to 59.

Output:

On the first line, print:

• "Late", if the student arrives later than the exam time;

• "On time", if the student arrives exactly on time or up to 30 minutes early;

• "Early", if the student arrives more than 30 minutes before the exam time.

If the student arrives at least a minute before the exam time, print on the next line:

• "mm minutes before the start" for arriving less than an hour early;

• "hh:mm hours before the start" for arriving 1 hour or more early. Always print minutes as 2 digits, e.g. "1:05";

• "mm minutes after the start" for being less than an hour late;

• "hh:mm hours after the start" for being 1 hour or more late. Always print minutes as 2 digits, e.g. "1:03".

########

09. Ski Trip:

Atanas decides to spend his vacation in Bansko and go skiing. Before he goes, however, he needs to book a hotel and calculate how much his stay will cost. The following types of rooms are available, with the following prices for stays:

▪ "room for one person" – 18.00 lv per night

▪ "apartment" – 25.00 lv per night

▪ "president apartment" – 35.00 lv per night

According to the number of days he will stay in the hotel (example: 11 days = 10 nights) and the type of room he will choose, he can use different discounts.

The discounts are as follows:

room for one person - no discount

apartment:

less than 10 days - 30% of the final price

between 10 and 15 days - 35% of the final price

more than 15 days - 50% of the final price

president apartment:

less than 10 days - 10% of the final price

between 10 and 15 days - 15% of the final price

more than 15 days - 20% of the final price

After the stay, Atanas's assessment of the hotel's services can be positive or negative. If his assessment is positive, Atanas adds 25% of the discount to the price with the discount already deducted. If his assessment is negative, he deducts 10%.

Input:

The input is read from the console and consists of three lines:

• First line - days of stay - integer in the range [0...365]

• Second line - type of room - "room for one person", "apartment" or "president apartment"

• Third line - rating - "positive" or "negative"

Output:

One line should be printed to the console:

• The price for his stay at the hotel, formatted to the second decimal place.

