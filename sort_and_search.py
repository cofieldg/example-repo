def binary_search(target, items): 
    low, high = 0, len(items) - 1 
 
    # Keep iterating until the low and high cross 
    while high >= low: 
        # Find midpoint 
        mid = (low + high) // 2 
 
        # If item is found at midpoint, return its index 
        if items[mid] == target: 
            return mid 
        # Else, if item at midpoint is less than target, 
        # search the second half of the list 
        elif items[mid] < target: 
            low = mid + 1 
        # Else, search the first half 
        else: 
            high = mid - 1 
 
    # Returns None if item not found 
    return None

# Insertion sort()
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Sequential search()
def sequential_search(target, items): 
    # Iterate over the list. If we find the target item, return its index. 
    for index in range(len(items)): 
        if items[index] == target: 
            return index 
    # If the target item is not found, return None. 
    return None 


myList = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9
result = binary_search(target, myList)

if result is not None: 
    print(f"Item {target} found at index {result}.") 
else: 
    print(f"Item {target} not found in the list.")

# Binary Search starts in the middle of the list, to instantly eliminate half 
# the elements in the list to search through.

# Insertion sort list
insertion_sort(myList)
print("Sorted list: ", myList)

# Sequetial sort to find 9
result = sequential_search(target, myList)

if result is not None: 
    print(f"Item {target} found at index {result}.") 
else: 
    print(f"Item {target} not found in the list.") 
