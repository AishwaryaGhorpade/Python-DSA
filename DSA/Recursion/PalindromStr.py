def palidrom(str,l,r):
    if l>=r:
        return True
    if str[l]!=str[r]:
        return False
    return palidrom(str,l+1,r-1)
st="aish"
print(palidrom(st,0,len(st)-1))

#time complexity half stack.