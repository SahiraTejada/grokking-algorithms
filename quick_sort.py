def quicksort(array):
    # If the array has 0 or 1 elements, it's already sorted (base case of recursion)
    if len(array) < 2:
        return array
    else:
        # Recursive case: choose the first element as the pivot
        pivot = array[0]

        # Create a sublist of all elements less than or equal to the pivot
        # These will go on the left side of the pivot in the final sorted array
        less = [i for i in array[1:] if i <= pivot]

        # Create a sublist of all elements greater than the pivot
        # These will go on the right side of the pivot in the final sorted array
        greater = [i for i in array[1:] if i > pivot]

        # Recursively sort the 'less' and 'greater' sublists
        # Then combine them with the pivot in the middle
        return quicksort(less) + [pivot] + quicksort(greater)

# Call the quicksort function with a sample list and print the result
print(quicksort([10, 5, 2, 3]))

    