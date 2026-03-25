def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)

print("Sorted list:", sorted_numbers)
