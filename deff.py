def my_split(text, delimiter):
    split_text = text.split(delimiter)
    return split_text

text = "hello my friend"
delimiter = " "
print(my_split(text, delimiter))

# print(my_split(text, delimiter) == text.split(delimiter))

def split(text, sep=" "):
    array = []
    index = 0

    for i in range(len(text)):
      if text[i] == sep:
        array.append(text[index:i])
        index = i + 1
    array.append(text[index:])
    return array

print(split("hello", "l"))