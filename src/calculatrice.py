from src import utils

MENU = (
    "Select operation:\n"
    "1) Add\n"
    "2) Subtract\n"
    "3) Multiply\n"
    "4) Divide\n"
)

def main():
    while True:
        print(MENU)
        choice = input("Enter choice (1-4): ").strip()

        # ✅ validate choice before asking for numbers
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1-4.\n")
            again = input("Another calculation? (y/n): ").strip().lower()
            if again != "y":
                break
            else:
                continue

        # ✅ safe number inputs
        try:
            a = float(input("Enter first number: ").strip())
            b = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        # ✅ perform operation
        try:
            if choice == "1":
                result = utils.add(a, b)
            elif choice == "2":
                result = utils.subtract(a, b)
            elif choice == "3":
                result = utils.multiply(a, b)
            elif choice == "4":
                result = utils.divide(a, b)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: division by zero")

        again = input("Another calculation? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
