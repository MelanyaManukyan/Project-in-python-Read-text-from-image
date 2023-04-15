# squares = [1, 2, 3] + ["hello"]
squares = [4, 16, "25"] * 2
print(squares) # slicing

removed_elem = squares.pop()
print(removed_elem)
print(squares)

index = squares.index("25")
print(index)