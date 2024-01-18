#Write a function which takes list, postion as i/p or parameter and remjove the elements in the given postion(it starts from 1)
def rem_pos(List,pos):
    l=len(List)
    for i in range(pos-1,l-1):
        List[i]=List[i+1]
    return List[0:l-1]
num=[8,1,34,7,0,2,10]
pos1=float(input("Enter the postion of element to remove:"))
pos=int(pos1) 
if(pos1==pos):
    l=len(num)
    if(pos>0 and pos<=l):
        print("After removing",rem_pos(num,pos))
    else:
        print(-1) 
else:
    print("please enter integer")              