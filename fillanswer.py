fill = "0"
diagonal = "x"
size = 4
# arr = [[fill] * size] * size
# print(arr)
for i in range(size): 
  ls = [fill] * size
  ls[i] = diagonal
  print(ls)

# or 
for i in range(size): 
  arr = [fill] * size
  arr[i] = diagonal
  row = " ".join(arr)
  print(arr)