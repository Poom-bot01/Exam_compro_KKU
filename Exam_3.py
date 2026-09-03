age = float(input("Enter your age: "))
price = 0 
if age < 0:
    print("Invalid age.")
elif age <= 12:
    price = 100
elif age <= 26:
    student = input("Are you a student? (Y/N): ").lower()
    Weekday = input("Is it a weekday? (Y/N): ").lower()
    if student == 'y' and Weekday == 'y':
        price = 150*0.8
    else:
        price = 150
elif age <= 59:
    price = 200
else:
    print("Senior always free!")
print (f"Price = {price:.2f} Baht.")
