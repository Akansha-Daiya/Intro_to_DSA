#Selection Sort in python
#time complexity is O(n*n)
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind+1,size):
            #select the minimum value in every iteration
            if array[j]<array[min_index]:
                min_index=j
            # Swapping the element to sort the array
            (array[ind], array[min_index]) = (array[min_index], array[ind])
    

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by Selection Sort: ')
print(arr)

