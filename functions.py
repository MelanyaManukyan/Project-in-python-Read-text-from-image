
def sub(iterible):
    sub_ = 0
    for num in iterible:
        sub_ -= num 
        return sub_
    
def say_hi():
    print("hi")

print(__name__)

if __name__ == "__main__":
    ls = [1, 2, 3]
    print(sub(ls))