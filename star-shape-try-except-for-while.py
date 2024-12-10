try:
    p = input("Enter a digit between 5 and 10 and press Enter: ")
    p = int(p)

    if not (5 <= p <= 10):
        print(f"{p} is not in the specified range! Please enter a digit between 5 and 10.")
    else:
        # Descending asterisk pattern
        for z in range(p, 0, -1):
            print(z * "*")

        # Separator
        print(p * "<->")

        # Ascending asterisk pattern
        for z in range(1, p):
            print(z * "*")

        # While loop to display decreasing pattern again
        while p > 0:
            print(p * "*")
            p -= 1

except ValueError:
    print("The input is not a valid number!")
