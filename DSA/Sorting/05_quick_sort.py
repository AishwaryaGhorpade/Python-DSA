def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quickSort(arr,low,high):
    if low>=high:
        return
    partitionIndex=partition(arr,low,high)
    quickSort(arr,low,partitionIndex-1)
    quickSort(arr,partitionIndex+1,high)
l=[4,5,9,6,10,1,7,2,8,3]
quickSort(l,0,len(l)-1)
print(l)