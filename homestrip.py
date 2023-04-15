def custom_strip(s):    
    start = 0
    end = len(s) - 1

    while start <= end and s[start].isspace():
        start += 1

    while end >= start and s[end].isspace():
        end -= 1

    return s[start:end + 1]

