# Tasks - Working with files

## 1. Top sales

The provided [CSV file](./realestatetransactions.csv) contains real estate transactions data. Write a program that reads the file, processes the data and prints the top five zip codes of the areas with the highest sales with the total sum of the sales.

Try to split the program into functions, if this is applicable.

The columns in the file are as follows:

1. Street
1. City
1. Zip
1. State
1. Beds
1. Baths
1. Square feet
1. Type
1. Sale date
1. Price

Example output:

```text
Zip code: 95757; Total: 12180045
Zip code: 95762; Total: 11309076
Zip code: 95823; Total: 10689826
Zip code: 95835; Total: 10222209
Zip code: 95758; Total: 10206647
```

Sample solution: [here](./real_estates.py).