def sum_iter(numbers_ls, a, b):
    sum_ = 0
    for number in numbers_ls:
        sum_ += number
    return sum_ + a + b


def say_hi():
    print("hi")

def say_hi_name(name):
    print(f"hi {name}")


say_hi()
say_hi_name("Viktor")

numbers = [1, 2, 3, 4]
n2 = [2, 6, 32]

numbers_s = sum_iter(numbers, 4, 5)
print(numbers_s)


s2_sum = sum_iter(n2, 1, 2)
print(s2_sum)