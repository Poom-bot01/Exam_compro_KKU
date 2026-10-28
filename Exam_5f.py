def get_input():
    s,a = input("Enter size and amount: ").split()
    a = int(a)
    if (s.lower() == "s" or s.lower() == "m" or s.lower() == "l") and a > 0:
        return s.upper(),a
    else:
        print("Invalid size or amount. Bye!")
        return "X", 0

def calc_price(s,a):
    if s == "S":
        price = 45
    elif s == "M":
        price = 55
    elif s == "L":
        price = 65
    total = price*a
    if a >= 5:
        total *= 0.9
    return total
