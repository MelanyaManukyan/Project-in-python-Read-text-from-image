# file = open("notes.txt", "w")
# file.write("hello world")
# file.close()

file = open("notes.txt", "r")
content = file.read()
file.close()
# print(content)


with open("with_notes.txt", "w") as file:
    file.write("1.2.3\n4.5.6")



with open("with_notes.txt", "r") as file:
    content = file.read()
    print(content)



with open("with_notes.txt", "a") as file:
    file.write("ggggg6")
