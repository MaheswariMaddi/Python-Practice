#calculator program usinf if condition
value1=float(input("enter the 1st value:"))  # 2
value2=float(input("enter the 2nd value:"))#5
string_name="""
select the opertaion serial no:
1:Add
2:Mul
3:Subtraction
4:Division
5:Exponent
"""
c=int(input(string_name))
if(c==1): #true
    add=value1+value2 #7
    print("addition",add)
elif(c==2):
    mul=value1*value2
    print("Multiplication",mul)
elif(c==3):
    sub=value1-value2
    print("subtraction:",sub)
elif(c==4):
    div=value1/value2
    print("division of two nois:",div)
elif(c==5):
    power=value1**value2
    power=(power)
    print("power of two",power)
elif(c>5):
    print("end")

