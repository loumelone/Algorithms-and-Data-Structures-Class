def merge(array, l, m, r): 
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1): 
        L[i] = array[l + i]
    for j in range(0, n2): 
        R[j] = array[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j <n2: 
        if L[i] <= R[j]: 
            array[k] = L[i]
            i += 1
        else: 
            array[k] = R[j]
            j += 1
        k += 1
    
        # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def merge_sort(array, l, r): 
    if l < r: 
        m = l+(r-l)//2

        merge_sort(array, l, m)
        merge_sort(array, m + 1, r) 
        merge(array, l, m, r)

array = [6,5,4,3,2,1]

r = len(array) - 1
merge_sort(array, 0, r)
print(array)
#first iteration - l = 0, m = 2
#merge_sort(0, 2)
    #m = 1
    #merge_sort(0,1)
        #m = 0 
        #merge_sort(0,0)
        #merge_sort(0,1)
            #m = 0
        #merge(0, 0, 1)
    #merge_sort(1,2)
        #m=1
        #merge_sort(1,1)
        #merge_sor(2,2)
        #merge(1, 1, 2)
    #merge(0,1,2)
#merge_sort(3, 5)
    #m = 4
    #sort(3,4)
        #m = 3
        #sort(3,3), #sort(4,4)
        #merge(3,3,4)
    #sort(4,5)
        #m = 4
        #merge(4,4,5)
    #merge(3,4,5)
#merge(0,2,5)
