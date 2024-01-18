#write a function to count the occurances of an element in the list without using built in method
def count_list(N,Num):
    x=0
    for i in Num:
        if(N==i):
            x=x+1 
    return x
N=float(input("Enter the no:"))
List=[4,2,0,56,21,76,44,3,2,6,4,7,2,0]
print(f"{N} count is:{count_list(N,List)}")
        