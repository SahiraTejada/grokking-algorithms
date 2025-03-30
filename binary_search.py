
def binary_search(arr, item):
    # Set the initial low index to 0 (start of the list)
    low = 0
    # Set the initial high index to the last index of the list
    high = len(arr) - 1
    # Continue looping as long as low index is less than or equal to high index
    # This means there is still a part of the list to search.
    while low <= high:
        # Calculate the middle index of the current search range
        mid = (low + high) // 2
        # Get the element at the middle index to compare with the target item
        guess = arr[mid]
        
        # Check if the middle element is equal to the item we're searching for
        if guess == item:
            # Return the index of the found item
            return mid
        # If the middle element is greater than the item, search in the lower half
        elif guess > item:
            high = mid - 1
        # If the middle element is less than the item, search in the upper half
        else:
            low = mid + 1
            
    # If the item was not found, return None
    return None

# Example usage
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list,2))

