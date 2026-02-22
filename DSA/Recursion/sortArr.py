#using 2 pointer

# def reverseaArr(arr,first,last):
#     if first>last:
#         return arr
#     arr[first],arr[last]=arr[last],arr[first]
#     return reverseaArr(arr,first+1,last-1)

def reverseArr(arr,i):
    if i>=len(arr)/2:
        return arr
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    return reverseArr(arr,i+1)


#using 1 pointer
arr=[1,2,3,4,5,6]
# print(reverseaArr(arr,0,len(arr)-1))     #calling 2variable  
print(reverseArr(arr,0))  
