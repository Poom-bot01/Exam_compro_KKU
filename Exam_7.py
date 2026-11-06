def print_menu(menu):
    print("----------")
    for i in menu:
        print(f"{i}\t\t {menu[i]}")
    print("----------")

# add menu    
menu = {"latte": 55, "americano": 45, "mocha": 60, "tea": 35}
print_menu(menu)
for i in range(2):
    drink, price = input("Enter name and price: ").split()
    price = int(price)
    if drink in menu:
        print("Drink already on the menu.")
    else:
        menu[drink] = price
print_menu(menu)

# get order
orders = []
drink, amount = input("Enter drink and amount (done 0 to stop): ").split()
while drink.lower() != "done":
    if drink in menu:
        amount = int(amount)
        tmp = [drink, amount]
        orders.append(tmp)
    else:
        print("Drink is not on the menu.")
    drink, amount = input("Enter drink and amount (done 0 to stop): ").split()

# print order
total = 0
print(f"---- {len(orders)} orders ----")
for i in range(len(orders)):
    print(f"{i+1}) {orders[i][1]} x {orders[i][0]}")
    total += orders[i][1] * menu[orders[i][0]]
print(f"Total price: {total:.2f}")
