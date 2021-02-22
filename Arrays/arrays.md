# Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1. The subarray which is already sorted.
2. Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

|                          |                  |                   |
| :----------------------: | :--------------: | :---------------: |
|  Best Case Performance   | O(n<sup>2</sup>) | comparison, swaps |
| Average Case Performance | O(n<sup>2</sup>) |                   |
|  Worse Case Performance  | O(n<sup>2</sup>) | comparison, swaps |
|     Space Complexity     |       O(1)       |     auxillary     |

# Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm

To sort an array of size n in ascending order:

1. Iterate from arr[1] to arr[n] over the array.
2. Compare the current element (key) to its predecessor.
3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

|                          |            |                       |
| :----------------------: | :--------: | :-------------------: |
|  Best Case Performance   |    O(n)    | Comparisons and swaps |
| Average Case Performance |   O(n^2)   |                       |
|  Worse Case Performance  |   O(n^2)   | Comparisons and swaps |
|     Space Complexity     | O(n), O(1) |   total, auxillary    |

# Quick Sort

Quicksort is a divide and conquer algorithm. It first divides the input array into two smaller sub-arrays: the low elements and the high elements. It then recursively sorts the sub-arrays. The steps for in-place Quicksort are:

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
   The base case of the recursion is arrays of size zero or one, which are in order by definition, so they never need to be sorted.

The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance

|                          |                    |                                                      |
| :----------------------: | :----------------: | :--------------------------------------------------: |
|  Best Case Performance   | O(n log n) or O(n) | simple partition, three-way partition and equal keys |
| Average Case Performance |     O(n log n)     |                                                      |
|  Worse Case Performance  |       O(n^2)       |                                                      |
|     Space Complexity     |      O(log n)      |                                                      |

# Merge Sort

|                          |            |                                                      |
| :----------------------: | :--------: | :--------------------------------------------------: |
|  Best Case Performance   | O(n log n) | simple partition, three-way partition and equal keys |
| Average Case Performance | O(n log n) |                                                      |
|  Worse Case Performance  | O(n log n) |                                                      |
|     Space Complexity     |    O(n)    |                   auxillary(naive)                   |

# Insertion Sort

# Heap Sort

|                          |            |                  |
| :----------------------: | :--------: | :--------------: |
|  Best Case Performance   |    O(n)    |                  |
| Average Case Performance | O(n log n) |                  |
|  Worse Case Performance  | O(n log n) |                  |
|     Space Complexity     |    O(1)    | auxillary(naive) |

# Bubble Sort

# Fast Sort

## Buck Sort

## Radix Sort

|                          |      |     |
| :----------------------: | :--: | :-: |
|  Best Case Performance   | O(n) |     |
| Average Case Performance | O(n) |     |
|  Worse Case Performance  | O(n) |     |
|     Space Complexity     | O(n) |     |

## Counting Sort

|                          |      |     |
| :----------------------: | :--: | :-: |
|  Best Case Performance   | O(n) |     |
| Average Case Performance | O(n) |     |
|  Worse Case Performance  | O(n) |     |
|     Space Complexity     | O(n) |     |
