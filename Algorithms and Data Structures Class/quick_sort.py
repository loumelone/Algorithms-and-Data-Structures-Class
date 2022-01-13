"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, l, r):
    print(r)
    pivot = r
    if l < r:
        for i in range(l, r + 1):
            if i < pivot:
                while array[i] > array[pivot]:
                    temp = array[pivot]
                    array[pivot] = array[i]
                    array[i] = array[pivot - 1]
                    array[pivot - 1] = temp
                    pivot -= 1 
                i += 1
    else: 
        return array
    quicksort(array, 0, pivot - 1)
    quicksort(array, pivot + 1, r)
    return array

test = [8, 7, 6, 5, 4, 3, 2, 1]
n = len(test) - 1
print quicksort(test, 0, n)