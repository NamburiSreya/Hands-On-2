B. Argue Selection Sort Correctness

The Selection Sort algorithm, despite its straightforward nature, requires careful evaluation, especially when applied to large datasets. This analysis delves into its validity and operational features.

Selection Sort operates by dividing the input array into sorted and unsorted sections. The algorithm's main steps involve scanning the unsorted section to find the smallest element, moving this element to the beginning of the unsorted section, and repeating this process until the entire array is sorted. The core idea is to iteratively extract and place the smallest elements from the unsorted section, thereby constructing a sorted sequence from left to right.

The correctness of Selection Sort can be demonstrated using the concept of loop invariance. At the start of each iteration, the algorithm ensures that the smallest unsorted element is correctly positioned. This iterative process continues until the entire array is sorted, guaranteeing that the algorithm will terminate with a correctly ordered sequence.

Selection Sort has a time complexity of O(n^2), where 'n' is the number of elements in the array. This quadratic complexity results from the need to find the minimum element in the unsorted section for each element in the array, potentially requiring 'n' comparisons in the worst case.

Although Selection Sort is correct, its quadratic time complexity limits its efficiency for large datasets. For extensive sorting tasks, more advanced algorithms like Merge Sort or Quick Sort, which have average-case time complexities of O(n log n), are generally more suitable. 

In summary, while Selection Sort's simplicity ensures its correctness, its efficiency limitations make it less ideal for large-scale data processing compared to more sophisticated sorting techniques.


C. System Specifications

System information: CPU: Windows 10.0.22621 Total RAM: 15.6 GB System: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

Storage information: C:\ - Total: 240.79 GB, Free: 89.09 GB D:\ - Total: 97.66 GB, Free: 97.54 GB E:\ - Total: 120.70 GB, Free: 120.55 GB 
