# solution 1

number = int(input("enter a number: "))

if number > 1:
    for i in range(2, number):
     if(number % i) == 0:
        print(False)
        break
    else:
       print(True)
else: 
   print(False)


# solution 2

number = int(input("enter a number: "))

is_prime = True
for i in range(2, int(number ** 0.5) + 1):
     if(number % i) == 0:
        is_prime = False
        break
else: 
   is_prime = False

print(is_prime)
