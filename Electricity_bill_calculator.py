def calculate_bill():
    units = float(input("Enter units consumed: "))
    rate = 50
    bill = units * rate
    print("Total electricity bill:", bill)

def main():
    while True:
        print("1. Calculate Bill")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            calculate_bill()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
