

def insertion_sort(lis):
    n = len(lis)
    for i in range(1, n):
        key_element = lis[i]
        j = i - 1
        while j >= 0 and lis[j] > key_element:
            lis[j + 1] = lis[j] 
            j -= 1
        lis[j + 1] = key_element
        print(lis)
    return lis

# Example usage
lis = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(lis)
print("Sorted array:", sorted_arr)
