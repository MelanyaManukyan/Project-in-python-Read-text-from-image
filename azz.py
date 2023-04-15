'(){[]}'

open = ['{', '(', '[']
close = ['}', ')', ']']

ls = ["[", "]", "{", "}", "(", ")"]

def is_correct(a):
    brackets = input("input brackets: ")
    for i in a:
        if brackets[0] == '(' and brackets[-1] == ')' or \
           brackets[1] == '{' and brackets[-2] == '}' or \
           brackets[2] == '[' and brackets[-3] == ']':
            return True
        else:
            return False
        
print(is_correct(input)) 
