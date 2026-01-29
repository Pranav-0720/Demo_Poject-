def add(a = 0,b = 0):
    print(" the sum is ", a + b)
def remainder( a = 0, b = 0):
    print("when a is divided by b then remainder is ", a % b)
def typenum(a, b):
    print("type of A is ", type(a))
    print("type of B is  ", type (b))
def campare(a = 34, b = 80):
    if(a > b):
        print(a," is greater than ",b)
    elif(a < b):
        print(b," is  greater than ", a)
    else:
        print("a is equal to b")
def average(a , b):
    c = (a + b)/2
    print("the average of two number is ",c)
def square(a  , b ):
    print("the square of A is ", pow(a,2))
    print("the square of B is ", pow(b , 2))
c = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))
add(c,b)
remainder(c,b)
typenum(c,b)
square(c,b)
average(c,b)