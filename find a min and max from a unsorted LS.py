# find a min and max from a unsorted list (linear search)

def minMax(lis):
    mini=lis[0]
    maxi = lis[0]
    for i in lis:
        if i <mini:
            mini=i
        if i > maxi:
            maxi=i
    return mini, maxi
lis=[23,46,4,21,325,4,7,774,32,21]
mini,maxi = minMax(lis)
print(f"minimum is {mini} and maximum is {maxi}")