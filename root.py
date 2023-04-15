# The root of number
number = 78996

digits_sum = 0

print(number)
number_length = len(str(number))
while number > 10:
    digits_sum += number % 10 # 0 + 6, 6 + 9, 15 + 9, 24 + 8, 32 + 7, -> 39 
    number //= 10   # 7899, 789, 78, 7
    if number < 10:
        # digits_sum += number
        # number = digits_sum
        number += digits_sum
        print(f"{number: ^{number_length}}")
        digits_sum = 0
        
    # print(number)

        
# Remove list element
arr = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# [Green', 'White', 'Black', 'Pink', 'Yellow']
# [Green', 'White', 'Black', 'Yellow']

# arr.pop(5)
# arr.pop(4)
# arr.pop(0)
arr.pop(0)
arr.pop(3)
arr.pop(3)

# print square array except first 5
arr = [i ** 2 for i in range(1, 31)]
print(arr[5:])

# 5. Write a Python program that make a list from given string
text = "helloooooo!"
arr =[]
for char in text:
    arr.append(char)

print(list(text))
print(arr)
