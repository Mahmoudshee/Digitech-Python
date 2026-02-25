def run_calculator():
    print("--- Professional Calculator ---")
    
    try:
        first_number = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number + second_number 
        elif operation == "/":
            result = first_number / second_number
        else:
            return

        print(f"The calculation result is: {result}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    run_calculator()
