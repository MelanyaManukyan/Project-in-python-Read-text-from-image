dictionary = {
    "x": list(range(11, 20)),
    "y": list(range(21, 30)),
    "z": list(range(31, 40))
}

x_value = dictionary["x"][4]
y_value = dictionary["y"][4]
z_value = dictionary["z"][4]

print(x_value)
print(y_value)
print(z_value)

print(f"x has value {dictionary['x']} y has the value {dictionary['y']} z has value {dictionary['z']}")