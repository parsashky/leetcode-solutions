def sum(a,b):
    return a+b
list1=[2,4,6,8,1,2]
list2=[1,3,5,7,9]    
list3 = []
while len(list1) != len(list2):
    if len(list1)>len(list2):
        list2.append(0)
    else:
        list1.append(0)
a =0
b = 0
result=list(map(sum,list1,list2))
for i in range(len(result)) :
    if result[i] >= 10 :
        a = (result[i] % 10 )+b
        list3.append(a)
        b = 0
        b = b + 1
    else :

        list3.append(result[i])

print(list3)

