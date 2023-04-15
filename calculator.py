def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

while True:
    try:
        expr = input("Enter an expression: ")
        a, op, b = expr.split()  
        a = float(a) 
        b = float(b)
        
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = sub(a, b)
        elif op == '*':
            result = mult(a, b)
        elif op == '/':
            result = div(a, b)
        else:
            raise ValueError("Invalid operator")
        
        print(f"{a} {op} {b} = {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
        
    except Exception as e:
        print(f"Error: {e}")
        
    else:
        break
