#print 1st and 2 nd and 3rd greatest no
a=100
b=200
c=69
if(a>b and a>c):
    print("a is great no")
    if(b>c):
        print("b is second largest no")
        print("c is third large no")
    else:
        print("c is second largest no")
        print("b is third large no")
if(b>c and b>a):
    print("b is great")
    if(c>a):
        print("c is second largest no")
        print("a is third large no")
    else:
        print("a is second largest no")
        print("c is third large no")
if(c>a and c>b):
    print("c is great")
    if(a>b):
        print("a is second largest no")
        print("b is third large no")
    else:
        print("b is second largest no")
        print("a is third large no")
        
        
          
    