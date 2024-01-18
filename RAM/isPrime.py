
def isPrime(n,m):
    """
        To check whether a number is prime or not
    Args:
        n (int): input to validate
    Returns:
        prime (bool): return value of the method
    """
    for i in range(2,n):
        if(n%i == 0):
            return False
    else:
        return True
    
    
print("Is prime No:",isPrime(3,5))    

def addNumbers(a,b):
    return a+b

c = addNumbers(1,2)
# Named Arguments
d = addNumbers(b =2, a= 9) 

x = addNumbers(-10,b=-2) 
print(c,d,x)

# Advantages:
# 1. Reusability
# 2. Modularity


# Primitive Type, by default follows Call by Reference,
# On assigning the new value, it won't modifies original variable memory loaction.

def testVar(a):
    print(a,id(a))
    a = 23
    print(a,id(a))
    
c = 2    
testVar(c)
print(c, id(c))


#Call by Reference
#For advanced data types, On adding data into same variable, it modifies orignal variable
def testList(fruits):
    fruits.append("Grapes")
    print(fruits, id(fruits))
    
summerFruits = ["Mango", "Orange"]
print(summerFruits, id(summerFruits))
testList(summerFruits)
print(summerFruits, id(summerFruits))


# Advanced Types, by default follows Call by Reference,
# On assigning the value, it won't modifies original variable.
def testList(summerFruits):
    summerFruits =  ("Mango","Orange")
    print(summerFruits, id(summerFruits))
    

summerFruits = ("Mango","Orange")
testList(summerFruits)
print(summerFruits, id(summerFruits))



# Variable length Arguments
def addNumbers(*args):
    sum = 0
    for a in args:
        sum += a
    
    return sum

print(addNumbers(1))
print(addNumbers(1,2))
print(addNumbers(1,2,3))
print(addNumbers(1,2,3,4))
print(addNumbers(1,2,3,4,5))



#Default Arguments
#all Default arguments should be at the end of all the non default arguments
def logX(x, base=10):
    print(x)
    print(base)
    print()
    return x+base

logX(5,2)
logX(5,10)
logX(6)


#Nested Functions
def outerFunction():
    print("Outer")
    
    def innerFunction():
        print("Inner")
    
    innerFunction()
    print("exit")
    
outerFunction()


#Nested Functions
def outerFunction():
    print("Outer")
    
    def innerFunction():
        print("Inner")
    
    print("exit")
    return innerFunction

print(outerFunction)    
a = outerFunction()
print(a)
a()


#One function for each Math operation, 2 arguments
#Calculate, 3 arguments, Calculate(2,5,"+")
#Factorial of a number





