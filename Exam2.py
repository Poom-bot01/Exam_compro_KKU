import math
r,h = input("Enter r and h: ").split()
am = int(input("Enter amount: "))
r = float(r)
h = float(h)
Cylinder = math.pi * (r ** 2) * h
ori_vol = Cylinder * am
left = ori_vol - (ori_vol * 0.15)
joan = ori_vol * 0.15

print(f"Original : {ori_vol:.2f}")
print(f"Leftover : {left:.2f}")
print(f"joan drink : {joan:.2f}")