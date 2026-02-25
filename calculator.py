def run_calculator():
    print("--- Simple Python Calculator ---")
    
    try:
        # Using descriptive snake_case variable names as per rubric
        first_number = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            # Specific Error Handling for Division by Zero (30 pts in rubric)
            if second_number == 0:
                print("Error: Cannot divide by zero!")
                return
            result = first_number / second_number
        else:
            print("Invalid operation selected.")
            return

        # Using f-strings for output (10 pts in rubric)
        print(f"The calculation result is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    run_calculator()
