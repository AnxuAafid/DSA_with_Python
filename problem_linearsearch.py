# write a program to return the indicies of all occurances of a number, using linear search

def occurance(lis , num):
    indeces=[]
    for i in range(len(lis)):
        if lis[i]==num:
            indeces.append(i)
    return indeces
lis = [4,4,5,6,7,85,4,3,2,4,5,6,7]
print(occurance(lis,4))