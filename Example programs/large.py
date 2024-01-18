list_num=[57,56,9,3,5,8,9,98,19,100]
b=list_num[0]
second_max=list_num[1]
for i in list_num:
    if (i>b):
        second_max=b
        b=i
    elif(i>second_max):
        second_max=i
print(second_max)