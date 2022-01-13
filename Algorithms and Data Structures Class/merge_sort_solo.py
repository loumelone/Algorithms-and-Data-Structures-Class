def merge(array, l, m, r): 
    n1 = m + 1 - l
    n2 = r - m 

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1): 
        L[i] = array[l + i]
    
    for j in range(0, n2):
        R[j] = array[m + 1 + j]
    
    k = l 
    i = j = 0 
    while i < n1 and j < n2: 
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else: 
            array[k] = R[j]
            j += 1
        k += 1
    
    #bit that handles remaining elements 
    #can only be from one of left or right
    while j < n2: 
        array[k] = R[j]
        j += 1
        k += 1
    
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

def merge_sort(array, l, r): 
    if l < r: 
        m = (l + r)//2

        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)
        print(array, l, m, r)

array = [21, 4, 1, 3, 9, 20, 25]
n = len(array) - 1
merge_sort(array, 0, n)
print(array)