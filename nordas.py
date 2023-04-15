ls = [89, 10, 76, 25, 100, 70]


counter = 0 

for i in range(len(ls)):
    is_swap = True
    for j in range(len(ls) - 1):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
            is_swap = False
    if is_swap:
        break



print(ls)