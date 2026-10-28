filename = input("Enter filename: ")
with open(filename, "r") as file:
    sell = file.readlines()
    items = 0
    revenue = 0
    for line in sell:
        item,sale,price = line.strip().split(",")
        sale = int(sale)
        price = float(price)
        items += 1
        revenue += price*sale
        print(f"Sale {item}: {sale:.0f} x {price:.2f}")
with open("report.txt", "w") as file:
    file.write(f"Items = {items:.0f}\nRevenue = {revenue:.2f}\n")
