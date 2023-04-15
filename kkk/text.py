text = "hello world"
new_text = ""

for char in text:
    if char.isalpha():
        possition = ord(char) + 3 # 68
        symbol = chr(possition)
        new_text += symbol
print(new_text)