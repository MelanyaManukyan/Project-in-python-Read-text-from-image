def encode(text):
    bin_str = " "
    for char in text:
        bin_str = bin_str + "{:08b}".format(ord(char))
    
    return bin_str

def decode(binary_string):
    chars_ls=[]
    for i in range(0, len(binary_string), 8):
     # print(i)
        chars_ls.append((chr(int(binary_string[i:i+8], 2))))
    return " ".join(chars_ls)        