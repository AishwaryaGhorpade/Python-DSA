def merge(left,right):
    l=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i<len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[j])
        j+=1
    return l
    
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[0:mid])
    right=mergeSort(arr[mid:])
    return merge(left,right)

l=[10,9,8,7,6,5,4,3,2,1]
print(mergeSort(l))