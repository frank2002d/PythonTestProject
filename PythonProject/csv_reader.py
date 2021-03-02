import csv

reader = csv.reader(open('inventory.csv'))

result = {}

for row in reader:
    key = row[0]
    print(key)
    if key in result:
        print('duplicate keys, please edit your inventory')
    result[key] = row[1:]
    print(result)

product_to_search = input('what is the product you want to search?: ')
value = result[product_to_search]
print(value)
print(f'the price of {product_to_search} is', value[0],'pesos only')
