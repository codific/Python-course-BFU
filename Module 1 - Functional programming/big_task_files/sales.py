from collections import defaultdict
from datetime import datetime

# Columns:
# transaction date, product name, price,
# payment type, customer name, city,
# state, country, account creation date, last login

FILENAME = './sales.csv'

TRANSACTION_INDEX = 0
PRICE_INDEX = 2
PAYMENT_TYPE_INDEX = 3
CITY_INDEX = 5
COUNTRY_INDEX = 7
TOTAL_KEY = 'total'

payment_types = {}
countries = defaultdict(dict)
dates = {}

with open(FILENAME, 'r') as f:
    for line in f:
        if line:
            line_parts = line.strip().split(',')

            price = float(line_parts[PRICE_INDEX])

            # Getting the payment type
            payment_type = line_parts[PAYMENT_TYPE_INDEX]
            payment_types[payment_type] = payment_types.get(payment_type, 0) + 1

            # Getting countries and cities
            country = line_parts[COUNTRY_INDEX]
            city = line_parts[CITY_INDEX]
            countries[country][TOTAL_KEY] = countries[country].get(TOTAL_KEY, 0) + price
            countries[country][city] = countries[country].get(city, 0) + price

            # Getting the transaction date
            transaction = line_parts[TRANSACTION_INDEX]
            transaction_date = transaction.split(' ')[0]
            month, day, year = transaction_date.split('/')
            year = 2000 + int(year)
            month = int(month)
            day = int(day)
            date = datetime(year=year, month=month, day=day)
            dates[date] = dates.get(date, 0) + price

sorted_payment_types = sorted(payment_types.items(), key=lambda x: x[1], reverse=True)
sorted_countries = sorted(countries.items(), key=lambda x: x[1][TOTAL_KEY], reverse=True)
sorted_dates = sorted(dates.items(), key=lambda x: x[1], reverse=True)

print('Payment types:')
print('=' * 30)
for payment, total in sorted_payment_types:
    print(f'Payment type: {payment} - {total}')

print('Top countries and top cities:')
print('=' * 30)
for country, cities in sorted_countries[:5]:
    country_total = cities[TOTAL_KEY]
    del cities[TOTAL_KEY]

    print(f'{country} - {country_total:.2f}')

    sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
    for city, city_total in sorted_cities[:5]:
        leading_intervals = ' ' * 5
        print(f'{leading_intervals}{city} - {city_total:.2f}')
    print('-' * 30)

print('Top days:')
for day, total in sorted_dates[:7]:
    print(f'{day:%d-%m-%Y (%A)} - {total:.2f}')