import P5f

if __name__ == "__main__":
    s,a = P5f.get_input()
    if s == "X":
        exit()
    else:
        total = P5f.calc_price(s,a)
        print(f"Your total is {total:.2f}")
        print("Thank you!")
