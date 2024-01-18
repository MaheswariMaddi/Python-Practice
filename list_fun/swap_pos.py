#write a fun which takes, list two integers as a input,swap the elements in the postions of the integers and return final list 
def swap(M,N,Num):
    temp=Num[M-1]
    Num[M-1]=Num[N-1]
    Num[N-1]=temp
    return Num
num=[2,5,6,9,0,13,90,78,34]
M1=float(input("Enter the 1st pos:"))
N1=float(input("Enter the 2nd pos:"))
l=len(num)
M=int(M1)
N=int(N1)
if(M1==M and N1==N and l>1):
    if((M>=1 and M<=l) and (N>=1 and N<=l)):
        print("final list",swap(M,N,num))
    else:
        print("Index is out of range")
else:
    print("only integers allowed")
                        