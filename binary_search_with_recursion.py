def binarySearch(lis,i,j,target):
    if i<=j:
        mid=(i+j)//2
        if lis[mid]==target:
            return mid
        elif lis[mid]<target:
            return binarySearch(lis,mid+1,j,target)
        else:
            return binarySearch(lis,i,mid-1,target)
    return -1
lis=[2,3,4,5,6,7,8,9,99]
res= binarySearch(lis,0,len(lis)-1,63)
if res != -1:
    print("The target is present at index: ",res)
else:
    print("target not found")        
