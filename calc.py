def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

num_1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num_2 = int(input("Enter second number: "))


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


operation_func = operations.get(operator, lambda: "Invalid operator")

result = operation_func(num_1, num_2)

print(f"{num_1} {operator} {num_2} = {result}")
