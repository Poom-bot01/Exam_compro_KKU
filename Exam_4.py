#Mango,Guava Who win?
n = int(input("Enter n: "))
for i in range(n):
    print(f"=== Round{i+1} ===")
    p1_input = input("Mango/Guava: ").lower()
    
    while True:
        if p1_input != "mango" and p1_input != "guava":
            print("xxx Invalid word xxx")
            p1_input = input("Mango/Guava: ").lower()
        else:
            break
        p2_input = input("Mango/Guava: ").lower()
        while True:
            if p2_input != "mango" and p2_input != "guava":
                print("xxx Invalid word xxx")
                p2_input = input("Mango/Guava: ").lower()
