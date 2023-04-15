a = 10 
b = 0
name = "bxdo"

try:
    c = a / b
    # a = x // 2
    # k = name[10]
    # a = x / 5

except (ZeroDivisionError, NameError, IndexError): # ditarki bolor depqery
    c = 0

finally:
    c = None
    print(c)

try:
    10 / 0
except ZeroDivisionError as err:
    print(err)

# raise
if b == 0:
    raise ValueError