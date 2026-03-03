def insertionSort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
l=[6,4,5,3,5,1,2]
print(insertionSort(l))

#time complexity of insertion sort for the worst case and average case is O(n^2)
#time complexity of insertion sort for the best case is O(n)