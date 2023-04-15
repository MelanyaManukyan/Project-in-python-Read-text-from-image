# text = "Hello"
# lower_text = text.lower()

# print(lower_text)

# numbers = "1234"
# print(numbers.isdigit())

"""

numbers = "1,234"
print(numbers.isdigit())
numbers = numbers + "ddd" 


numbers = "1,23,4,,"
number = numbers.replace(",","", 1)
print(number)


text = "hello world"
print(text.title())
print(text.capitalize())



username = " mammamia2023 "
print(username.strip())
print(username)
"""

def is_balanced(s):
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack:
                return False
            if c == ')' and stack[-1] == '(' or \
               c == '}' and stack[-1] == '{' or \
               c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

# example usage:
print(is_balanced("({[]})")) # True
print(is_balanced("({[}])")) # False
