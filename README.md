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

Schreiben Sie ein Programm, das zwei ganze Zahlen (N1 und N2) und einen Operator liest, um eine bestimmte mathematische Operation auszuführen. Mögliche Operationen sind: Addition(+), Subtraktion(-), Multiplikation(*), Division(/) und Modulare Division(%). Beim Addieren, Subtrahieren und Multiplizieren sollte die Konsole das Ergebnis und die Angabe, ob es gerade oder ungerade ist, ausgeben. Bei der gewöhnlichen Division ist das Ergebnis. In modularer Aufteilung - der Rest. Es ist zu beachten, dass der Divisor gleich 0 (Null) sein kann und nicht durch Null teilbar ist. In diesem Fall muss eine besondere Meldung aufgedruckt werden.

Input:

3 vom Benutzer eingegebene Zeilen werden aus der Konsole gelesen:
 • N1 – Ganzzahl;
 • N2 – Ganzzahl;
 • Operator – ein Zeichen aus der Auswahl: „+“, „-“, „*“, „/“, „%“.
 
Output:

So drucken Sie eine Zeile auf der Konsole:
 • Wenn es sich bei der Operation um Addition, Subtraktion oder Multiplikation handelt:
 ◦ "{N1} {Operator} {N2} = {Ergebnis} - {gerade/ungerade}"
 • Wenn es sich bei der Operation um eine Division handelt:
 ◦ "{N1} / {N2} = {Ergebnis}" - Ergebnis auf die zweite Dezimalstelle formatiert
 • Wenn es sich um eine modulare Aufteilung handelt:
 ◦ "{N1} % {N2} = {Rest}"
 • Im Falle einer Division durch 0 (Null):
 ◦ „{N1} kann nicht durch Null geteilt werden“
Beispiele für Eingabe und Ausgabe

########

