def bubble_sort(array): 
    for i in range(0, len(array) - 1):
        j = i + 1
        if array[i] > array[j]:
            num = array[j]
            array[j] = array[i] 
            array[i] = num 
    print(array)
    for i in range(0, len(array) - 1): 
        j = i+1
        if array[i] > array[j]: 
            return bubble_sort(array)
    return array

array = [21,4,1,3,9,20,25,6,21,14]
print(bubble_sort(array))