from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number: float | None = None
continue_from_last = False
more_operations = True
while more_operations:
    print(logo)
    if first_number and continue_from_last:
        print(f"The first number is {first_number}")
    else:
        first_number = float(input("What is the first number?: "))

    for operator in operations:
        print(operator)
    operation = input("Please select an operation to perform from above: ")
    second_number = float(input("What is the second number?: "))

    if operation in operations:
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        go_again = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        ).lower()
        if go_again == "y":
            continue_from_last = True
            first_number = result
        else:
            continue_from_last = False
    else:
        print("Please select a valid operation!")
