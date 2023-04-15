def is_valid(a):
    if "." not in a:
        return False
    
    numbers = a.split(".")
    if len(numbers) > 2:
        return False
    
    for num in numbers:
        if not num.isdigit():
            return False
    else:
        return True
    

print(is_valid("2.5"))
print(is_valid("2.4.4"))
print(is_valid("i3.4"))

