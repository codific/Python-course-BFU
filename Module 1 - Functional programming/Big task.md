# Big task - end of Functional programming

The provided [CSV file](./big_task_files/sales.csv) contains some sanitized sales transactions during the month of January 2009.

Write a program that reads the file, processes the data and outputs several statistics:

1. The total number of each payment type used to make a transaction, sorted in decreasing order.
1. The top 5 countries and top 5 cities (if there are less than 5 cities, just extract all of them) of each country with most purchases (total price, not total count), sorted in decreasing order.
1. The top seven days of the month with highest sales.

*Note:* Try to split the program into functions, if this is applicable.

The columns in the file are as follows:

1. Transaction date
1. Product name
1. Price
1. Payment type
1. Customer name
1. City
1. State
1. Country
1. Account creation date
1. User last login

Sample output:

```text
Payment types:
==============================
Payment type: Visa - 522
Payment type: Mastercard - 277
Payment type: Amex - 110
Payment type: Diners - 89

Top countries and top cities:
==============================
United States - 750000.00
     New York - 15600.00
     Centennial - 15400.00
     Fresno - 9900.00
     Seattle - 9600.00
     Arlington - 9200.00
------------------------------
United Kingdom - 144000.00
     London - 30000.00
     Kirriemuir - 7200.00
     New Malden - 3600.00
     Edinburgh - 3600.00
     Guildford - 3600.00
------------------------------
Canada - 124800.00
     Toronto - 16800.00
     Calgary - 15600.00
     Vancouver - 12000.00
     Ottawa - 7200.00
     Okotoks - 4800.00
------------------------------
Switzerland - 76800.00
     Lausanne - 7200.00
     Zug - 4800.00
     Zurich - 4800.00
     Binningen - 3600.00
     Bellinzona - 3600.00
------------------------------
Ireland - 69900.00
     Navan - 7500.00
     Cork - 7200.00
     Castleknock - 3600.00
     Clondalkin - 3600.00
     Clontarf - 2400.00
------------------------------

Top days:
25-01-2009 (Sunday) - 81300.00
18-01-2009 (Sunday) - 80700.00
07-01-2009 (Wednesday) - 79200.00
12-01-2009 (Monday) - 73500.00
05-01-2009 (Monday) - 72300.00
06-01-2009 (Tuesday) - 72000.00
11-01-2009 (Sunday) - 59100.00
```