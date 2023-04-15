rooms = {1: "python", 2: "java", 9: "js"}

for key in rooms:
    print(rooms[key])

print("=" * 30)
for value in rooms.values():
    print(value)

a = 2, 3 # -> tuple
a, b = (2, "dfasf")
ls = [(1, "pythin"), (2, "java"), (3, "js")]
# a, b = ls[0]

for item in ls:
    print(item)