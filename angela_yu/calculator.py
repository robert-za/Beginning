from calculator_art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
              "+": add,
              "-": sub,
              "*": mul,
              "/": div
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    calculating = True
    while calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ") == "y":
            num1 = answer
        else:
            calculating = False
            calculator()

calculator()