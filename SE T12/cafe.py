# list of menu items
menu = ['tea', 'coffee', 'milk', 'water']
# dictionary of stock with stock number
stock = {'tea' : 1,
         'coffee' : 1,
         'milk' : 1,
         'water' : 1
         }
# dictionary of stock items and price in arbitary currency
price = {'tea' : 1.,
         'coffee' : 1.,
         'milk' : 1.,
         'water' : 1.}

total_stock = 0
for i in range(len(menu)):
    total_stock += stock[menu[i]]*price[menu[i]]

print(total_stock)