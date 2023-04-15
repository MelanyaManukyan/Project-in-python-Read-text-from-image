def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


operators = []
numbers = []


while True:
     input_ = input("Enter number or operator: ")
     
     if input_ == "=":
         break
     if input_ in ["+", "-", "*", "/"]:
         operators.append(input_)
     else:
         numbers.append(int(input_))

expression = " "
for i in range(len(numbers)):
    expression += str(numbers[i])
    if i < len(operators):
        expression += " " + operators[i] + " "

for i in range(len(operators)):
    operator = operators[i]
    num = numbers[i + 1]

    if operator == "*":
        numbers[i] = mult(numbers[i], num)
        numbers[i + 1] = None
        operators[i] = None
    elif operator == "/":
        numbers[i] = div(numbers[i], num)
        numbers[i + 1] = None
        operators[i] = None

numbers = [num for num in numbers if num is not None]
operators = [op for op in operators if op is not None]
    
result= numbers[0]

for i in range(len(operators)):
    operator = operators[i]
    num = numbers[i + 1]

    operation_func = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div
    }[operator]
    result = operation_func(result, num)


print(f"{expression} = {result}")


