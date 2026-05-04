#assumption: arr is a list
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # [1, 2, 3] -> 0,1,2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


data = [1,2,3,4,5,6,7,8]
found_idx = binary_search(data, 10)




def binary_search(arr, target, op='first'):
    low = 0
    high = len(arr) - 1 # [1,2,3] -> 0,1,2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if op == 'first':
                while mid - 1 >= 0 and arr[mid - 1] == target:
                    mid -= 1
            elif op == 'last':
                while mid + 1 < len(arr) and arr[mid + 1] == target:
                    mid += 1
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

