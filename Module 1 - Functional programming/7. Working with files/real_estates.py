#!/usr/bin/env python

# Columns
# street, city, zip, state, beds, baths, sq__ft, type, sale_date, price

FILENAME = './realestatetransactions.csv'
ZIP_INDEX = 2
PRICE_INDEX = 9

zip_codes = {}

with open(FILENAME, mode='r', encoding='utf-8') as f:
    for line in f:
        if line:
            line_parts = line.strip().split(',')
            zip_code = line_parts[ZIP_INDEX]
            price = float(line_parts[PRICE_INDEX])
            zip_codes[zip_code] = zip_codes.get(zip_code, 0) + price

sorted_result = sorted(zip_codes.items(), key=lambda x: x[1], reverse=True)

for item in sorted_result[:5]:
    zip_code, total = item
    print("Zip code: {zip_code}; Total: {total:.2f}".format(
        zip_code=zip_code,
        total=total
    ))
