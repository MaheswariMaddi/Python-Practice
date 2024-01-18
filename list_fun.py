list=["Mahi"," ram","shyam"]

for i in range(len(list)-1):
    if(list[i]<list[i+1]):
        list[i]=list[i]
    else:
        list[i]=list[i+1]
print(list)        