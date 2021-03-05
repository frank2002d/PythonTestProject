import csv

reader = csv.reader(open('inventory.csv'))

inventory_ko = {}

for row in reader:
    key = row[0]
    # print(key)  #print the keys found every loop
    if key in inventory_ko:
        print('''
        duplicate keys found!!! Please edit your inventory

        ''')
    inventory_ko[key] = row[1:]
    # print(inventory_ko)


#
# product_to_search = input('what is the product you want to search?: ')
# value = inventory_ko[product_to_search]
# print(value)fish
# print(f'the price of {product_to_search} is', value[0],'pesos only')

def search_product():
    global product_to_search
    product_to_search = input('what is the product you want to search?: ')
    if product_to_search in inventory_ko.keys():
        return True
    else:
        return False


# this code searches for the product and its corresponding price


repeat = True                   # initial value of repeat = true
found = search_product()  #create found variable for the status of search_prod

while repeat == True:
    if found == True:
        print('value found')
        value = inventory_ko[product_to_search]
        print(f'the price of {product_to_search} is', value[0], 'pesos only')
        print()
        search_again = input('would you like to try again y/n?  ')

        if search_again == 'y' or search_again == 'Y':
            repeat = True
            found = search_product()
        else:
            repeat = False
            break

    else:
        print('not found')
        found = search_product()
        repeat = True
