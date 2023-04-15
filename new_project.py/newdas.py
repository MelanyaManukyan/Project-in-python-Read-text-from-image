ls = [1, 2, 3, "342"]

def sum_elem(ls):
    sum_elem = 0
    for num in ls:
        if isinstance(num, str) and num.isdigit():
            sum_elem += int(num)
        elif isinstance(num, int):
            sum_elem += num 
    return sum_elem

# 