import math
y = max(1,2,3,4,5,6,7)

def printme(str):
    "Print a name on the screen"
    print(str)
    return

printme("Praveen")


def greet(name):
    print("Hello, " + name)

greet("Nimal")

def circum(r):
    "Calculate circumference and return"
    return 2* math.pi *r

print(circum(2))
print(circum.__doc__)


print(y)