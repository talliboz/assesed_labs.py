def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2

    # Function implementation here ...
def perform_operation(num1, num2, operator):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        elif operator == "%":
            # Modulo by zero check
            if num2 == 0:
                return "Error: Modulo by zero is not allowed."
            return num1 % num2
        elif operator == ">":
            return num1 > num2
        elif operator == ">=":
            return num1 >= num2
        elif operator == "<":
            return num1 < num2
        elif operator == "<=":
            return num1 <= num2
        else:
            return f"Error: Unknown operator '{operator}'"
    except Exception as e:
        return f"Error: {str(e)}"


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %, >, >=, <, <=): ")


result = perform_operation(num1, num2, operator)
print("Result:", result)
## Run the example
# calculator(4, 5, "*")  # Output: The result is: 20
# calculator(10, 2, "/")  # Output: The result is: 5.0
# calculator(7, 7, ">=")  # Output: The comparison result is: True