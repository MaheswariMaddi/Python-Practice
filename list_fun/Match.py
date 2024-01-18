#Write a function that two lists have at one common no returns true oterwose reutn false.
def match(m,n):
    for i in m:
        for j in n:
            if(i==j):
                return True
    return False
M=[2,3,4,5,0,9,8,7,2,1]
N=90,12,45,67,89,34,56
l=len(M) 
l1=len(N)
if((M==N) or (l==0 and l==0)):
    print(True)
elif(l>0 and l1>0):
    print("Match is found",match(M,N))
else:
    print(False)                       
            