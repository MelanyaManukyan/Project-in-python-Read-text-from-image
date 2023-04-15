
# number = "{:=^10}".format(5)
# number_2 = "{:<^10}".format(43255)
# print(number)
# print(number_2)



pound = 2.2

for i in range(1, 100, 2):
    p = i * pound 
    print("{: >3}: {: ^4.1f}".format(i, p))