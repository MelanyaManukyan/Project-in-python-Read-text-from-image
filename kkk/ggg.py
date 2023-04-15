number = 0

counter = 0

while number < 100:
    counter += 1 
    number += 1
    if number == 4 or number == 6:
        continue
    elif number == 8:
        break
    print(counter, "number: ", number)
    number += 1
