def selectionSort(num):
    for i in range(len(num)):
        minIdex=i
        for j in range(i+1,len(num)):
            if num[j]<num[minIdex]:
                minIdex=j
        num[i],num[minIdex]=num[minIdex],num[i]
    return num
l=[5,4,3,2,1]
print(selectionSort(l))