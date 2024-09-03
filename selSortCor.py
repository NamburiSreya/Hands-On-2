# Selection Sort Implementation

def selection_sort(data):
    length = len(data)
    for start in range(length):
        # Assume the first unsorted element is the smallest
        smallest_index = start
        # Find the actual smallest element in the remaining unsorted array
        for current in range(start + 1, length):
            if data[current] < data[smallest_index]:
                smallest_index = current
        # Swap the found smallest element with the first unsorted element
        data[start], data[smallest_index] = data[smallest_index], data[start]

# Example Usage
numbers = [73, 18, 55, 39, 6]
selection_sort(numbers)
print("Sorted list:", numbers)