# Function to find the index of the smallest element in a list
def findSmallest(arr):
    smallest = arr[0]               # Assume the first element is the smallest
    smallest_index = 0              # Save the index of the smallest element
    for i in range(1, len(arr)):    # Loop through the rest of the array
        if arr[i] < smallest:       # If we find a smaller element
            smallest = arr[i]       # Update the smallest value
            smallest_index = i      # Update the index of the smallest value
    return smallest_index           # Return the index of the smallest element found


# Function that performs selection sort and returns a new sorted list
def selectionSort(arr):  
    newArr = []                              # This will store the sorted elements
    copiedArr = list(arr)                    # Make a copy of the original array so we don't change the input
    for i in range(len(copiedArr)):          # Repeat as many times as there are elements
        smallest = findSmallest(copiedArr)   # Find the index of the smallest element in the remaining list
        newArr.append(copiedArr.pop(smallest)) # Remove the smallest element from copiedArr and add it to newArr
    return newArr                             # Return the fully sorted array


# Test the selectionSort function
print(selectionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]
