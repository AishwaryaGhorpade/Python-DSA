def PalindronString(str,left,right):
    if str[left]!=str[right]:
        return False
    if left>=right:
        return True
    return PalindronString(str,left+1,right-1)
str1=input("enter a string: ")
len=len(str1)
print(PalindronString(str1,0,len-1))