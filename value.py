dict = {}
start = int(input("enter your first number: "))
end = int(input("enter your last number: "))

for i in range(start, end + 1):
    dict[i] = i ** 2

print(dict)

