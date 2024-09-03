import timeit as chronometer
import platform as sys_platform
import psutil as sys_monitor
import random as randomizer
import matplotlib.pyplot as vis

# Hardware Diagnostics
def cpu_info():
    return f"Processor: {sys_platform.processor()}"

def memory_status():
    mem = sys_monitor.virtual_memory()
    return f"Available Memory: {mem.available / (1024**3):.2f} GB"

def storage_details():
    drives = sys_monitor.disk_partitions()
    storage = []
    for drive in drives:
        usage = sys_monitor.disk_usage(drive.mountpoint)
        storage.append(f"{drive.device} - Capacity: {usage.total / (1024**3):.2f} GB, Free: {usage.free / (1024**3):.2f} GB")
    return storage

def os_info():
    return f"Operating System: {sys_platform.system()} {sys_platform.version()}"

# Sorting Algorithms
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

# Utility Functions
def generate_dataset(size):
    return [randomizer.randint(1, 5000) for _ in range(size)]

def measure_performance(algorithm, dataset):
    setup = f"from __main__ import {algorithm}, generate_dataset; data = generate_dataset({len(dataset)})"
    stmt = f"{algorithm}(data)"
    execution_time = chronometer.timeit(stmt, setup=setup, number=5)
    return execution_time

# Benchmark Configuration
dataset_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

# Performance Tracking
algorithm_performance = {
    'Insertion Sort': [],
    'Selection Sort': [],
    'Bubble Sort': []
}

# Benchmark Execution
for size in dataset_sizes:
    dataset = generate_dataset(size)

    for algo in ['insertion_sort', 'selection_sort', 'bubble_sort']:
        perf_time = measure_performance(algo, dataset)
        algorithm_performance[algo.replace('_', ' ').title()].append(perf_time)

# System Diagnostics Output
print("System Diagnostics:")
print(cpu_info())
print(memory_status())
print(os_info())

print("\nStorage Overview:")
print('\n'.join(storage_details()))

# Visualization
vis.figure(figsize=(12, 7))
for algo, times in algorithm_performance.items():
    vis.plot(dataset_sizes, times, label=algo, marker='o')

vis.xlabel('Dataset Dimension')
vis.ylabel('Execution Duration (seconds)')
vis.title('Sorting Algorithm Efficiency Analysis')
vis.legend()
vis.grid(True)
vis.xscale('log')
vis.yscale('log')
vis.show()
