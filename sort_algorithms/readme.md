# Sort Algorithms
This projects covers the implementation of the most popular sort algorithms, their description and their various implementations using python. 
Feel free to contribute to the project implementations in other languages

## Quick Sort Algorithm
`time complexity`: It has a worst case running time of O(n2), but the average case running time is O(nlog(n)) where n is the length of the input to be sorted.
`space complexity`: The in-place version of quicksort has a space complexity of O(log n), even in the worst case. However, the recursive calls, in the worst case quicksort could make O(n) nested recursive calls and need O(n) auxiliary space.

`how it works`: The quick sort algorithm makes use of the divide and conqueer approach to solve sorting problems. Taking the array/list provided, the algorithm selects a random value from the list/array as the value for comparison, a pivot which acts as the central point. Using this value it runs through the list/array and places the values in the appropriate side of the pivot, either to the list/array on the left which has values less than the pivot value or the list/array on the right which has greate values. This algorithm is recursive, this means that the left and right subarrays/sublists undergo the same process till they are all sorted.


## Bubble Sort
`time complexity`: The best case time complexity of bubble sort is O(n) and the worst case time complexity is O(n^2), which also happens to be the average case time complexity of bubble sort, this makes it one of the slower sorting algorithms around.

`space complexity`: The space complexity of bubble sort is O(1)

`how it works`: It is an inplace sorting algorithm and is considered as one of the easiest algorithms to implement. With the use of nested loops, the array/list provided is gone through several times, such that the outer loop selects an initial element and the inner loop goes through all elements in the array and constantly checks for the smallest element and exchanges it with the element selected by the outer loop, this continues until the array/list is sorted