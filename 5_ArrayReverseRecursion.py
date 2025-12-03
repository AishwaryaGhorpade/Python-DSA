# reverse the array from left to right only
# num=[1,2,3,4,5,6],left=2 ,right=4 
# output=[1,2,,5,4,3,6]

def ArrayReverse(num,left,right):
    if left>=right:
        return num
    num[left],num[right]=num[right],num[left]
    ArrayReverse(num,left+1,right-1)

arr=[1,2,3,4,5,6]
left=2
right=4
print("Before:",arr)
ArrayReverse(arr,left,right)
print("After: ",arr)


# Time complexity is O(1/2 N) i.e almost O(N) & stack space is O(N/2) i.e O(N) 

# output. l=0 ,r=5
# Before: [1, 2, 3, 4, 5, 6]
# After:  [6, 5, 4, 3, 2, 1]

# left=2,right=4
# Before: [1, 2, 3, 4, 5, 6]
# After:  [1, 2, 5, 4, 3, 6]