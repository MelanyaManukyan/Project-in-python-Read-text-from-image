def a(text):
    print("function a", text)

def b(text):
     print("function b", text)

def c(text):
     print("function c", text)

# par_ = input("input func name:")
# print(locals())
 
inp = input() # a  args
locals()[inp[0]](inp[2:])

print(inp)