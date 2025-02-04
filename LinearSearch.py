def linearSearch(target):
    lis=[23,45,67,68,85,543]

    for i in lis:
        if i ==target:
            print("Found")
            return i
    return -1
res = linearSearch(int(input("enter no. to be found: ")))
if res!= -1:
    print("The index is present at index ",res)
else:
    print("not found")