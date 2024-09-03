import timeit
import platform as machine
import psutil as system_info
import random as chance
import matplotlib.pyplot as plt

# Machine Specifications
def fetch_processor():
    return f"Processor: {machine.processor()}"

def fetch_memory():
    mem = system_info.virtual_memory()
    return f"Total Memory: {mem.total // (1024**3)} GB"

def fetch_disk_space():
    disks = system_info.disk_partitions()
    space_info = []
    for disk in disks:
        usage = system_info.disk_usage(disk.mountpoint)
        space_info.append(f"{disk.device} - Capacity: {usage.total // (1024**3)} GB, Available: {usage.free // (1024**3)} GB")
    return space_info

def fetch_os():
    return f"Operating System: {machine.system()} {machine.release()}"

# Quick Sort
def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Insertion Sort
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Selection Sort
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# Generate random dataset
def create_dataset(size):
    return [chance.randint(1, 5000) for _ in range(size)]

# Measure algorithm performance
def measure_performance(sort_algo, dataset):
    setup = f"from __main__ import {sort_algo}, create_dataset; data = create_dataset({len(dataset)})"
    command = f"{sort_algo}(data)"
    execution_time = timeit.timeit(command, setup=setup, number=5)
    return execution_time

# Test parameters with starting sizes
dataset_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

# Store performance results
performance_data = {'Quick Sort': [], 'Insertion Sort': [], 'Selection Sort': []}

# Conduct performance tests
for size in dataset_sizes:
    dataset = create_dataset(size)

    # Quick Sort
    quick_time = measure_performance('quick_sort', dataset)
    performance_data['Quick Sort'].append(quick_time)

    # Insertion Sort
    insertion_time = measure_performance('insertion_sort', dataset)
    performance_data['Insertion Sort'].append(insertion_time)

    # Selection Sort
    selection_time = measure_performance('selection_sort', dataset)
    performance_data['Selection Sort'].append(selection_time)

# Display machine specifications
print("Machine Specifications:")
print(fetch_processor())
print(fetch_memory())
print(fetch_os())

print("\nStorage Details:")
print('\n'.join(fetch_disk_space()))

# Visualize performance results
plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, performance_data['Quick Sort'], label='Quick Sort', marker='o')
plt.plot(dataset_sizes, performance_data['Insertion Sort'], label='Insertion Sort', marker='s')
plt.plot(dataset_sizes, performance_data['Selection Sort'], label='Selection Sort', marker='^')

plt.xlabel('Dataset Size')
plt.ylabel('Execution Duration (seconds)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()