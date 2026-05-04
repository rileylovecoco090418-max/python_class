def bubble_sort(my_array):
    n = len(my_array)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if my_array[j] > my_array[j+1]:
                # Swap if the element found is greater than the next
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

    
def selection_sort(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    return my_array
    
def insertion_sort(my_array):
    for i in range(1, len(my_array)):
        key = my_array[i]
        j = i - 1
        # Move elements of my_array[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < my_array[j]:
            my_array[j + 1] = my_array[j]
            j -= 1
        my_array[j + 1] = key
    return my_array

#  Test code
if __name__ == '__main__':
    test_data1 = [8, 2, 6, 4, 5]
    sorted_test_data1 = insertion_sort(test_data1)

