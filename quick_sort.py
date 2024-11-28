def quick_sort(arr):
    # Base case: Arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (typically the last element)
    pivot = arr[-1]

    # Partition: Divide array into two lists: less than and greater than the pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]  # Elements <= pivot
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]  # Elements > pivot

    # Recursively sort the partitions and concatenate with the pivot
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
