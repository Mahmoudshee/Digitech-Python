def run_calculator():
    print("--- Simple Python Calculator ---")
    
    try:
        # VIOLATION 1: Using non-descriptive names 'a' and 'b' (Deduce points)
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            # VIOLATION 2: No check for b == 0 (Major deduction per rubric)
            res = a / b
        else:
            print("Invalid")
            return

        # VIOLATION 3: Using old string concatenation instead of f-strings
        print("The calculation result is: " + str(res))

    except ValueError:
        print("Error!")

if __name__ == "__main__":
    run_calculator()
