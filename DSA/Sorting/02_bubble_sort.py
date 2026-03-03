def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
l=[5,4,3,2,1,6,7,0,-3]
print(bubbleSort(l))

# Time complexity for average and worst case -->O(N^2)
# Time complexity for best case(when arr is already sorted) -->O(N)