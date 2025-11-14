a = 0
b = 0
list1=[2,4,6,8,1,2]
list2=[1,3,5,7,9]   
result=list(map(sum,list1,list2))
for i in range(len(result)) :
    if i >= 10 :
        a = i % 10 
        b = result[i+1] +1
        result.insert(i+1,b)

print(result)