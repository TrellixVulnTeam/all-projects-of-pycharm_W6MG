import sys
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print("hello",i)
    greet()

greet()