ls = [1, 2, 3, 54, 234, 5436]

for num in ls:
    print(num)

# or

i = 0
while i < len(ls):
    print(ls[i])
    i += 1





# ex 1

def kg_to_lb(kg):
    return kg * 2.2

print("kilograms in pounds")
for i in range(1, 200, 2):
    print(i, kg_to_lb(i))


# ex 2

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([8, 2, 3, -1, 7]))
print(multiply_list([2, 3, 4, 5, 2]))