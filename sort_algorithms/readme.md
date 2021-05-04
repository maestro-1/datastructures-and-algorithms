# Sorting Algorithms
This projects covers the implementation of the most popular sort algorithms, their description and their various implementations using python. 
Feel free to contribute to the project implementations in other languages. 

## Quick Sort
`time complexity`: It has a worst case running time of O(n2), but the average case running time is O(nlog(n)) where n is the length of the input to be sorted.

`space complexity`: The in-place version of quicksort has a space complexity of O(log n), even in the worst case. However, the recursive calls, in the worst case quicksort could make O(n) nested recursive calls and need O(n) auxiliary space.

`how it works`: The quick sort algorithm makes use of the divide and conqueer approach to solve sorting problems. Taking the array/list provided, the algorithm selects a random value from the list/array as the value for comparison, a pivot which acts as the central point. Using this value it runs through the list/array and places the values in the appropriate side of the pivot, either to the list/array on the left which has values less than the pivot value or the list/array on the right which has greate values. This algorithm is recursive, this means that the left and right subarrays/sublists undergo the same process till they are all sorted.


## Bubble Sort
`time complexity`: The best case time complexity of bubble sort is O(n) and the worst case time complexity is O(n^2), which also happens to be the average case time complexity of bubble sort, this makes it one of the slower sorting algorithms around.

`space complexity`: The space complexity of bubble sort is O(1)

`how it works`: It is an inplace sorting algorithm and is considered as one of the easiest algorithms to implement. With the use of nested loops, the array/list provided is gone through several times, the each element is compared to its succeeding element: each index is compared to index + 1. If the selected element is greater than the succeeding element then their positions are exchanged, and this is repeated until the entire list/array is sorted.

## Selection Sort
`time complexity`: The time complexity for selection, both best and worse case, is 0(n^2) 

`space complexity`: The space complexity of selection sort is 0(1). Selection sort never makes more than O(n) swaps, hence it is good when memory usage is an important factor

`how it works`: Selection sort makes use of sorted algorithms to sort given lists/arrays. The difference between selection sort and bubble sort is how it interacts with the list/array it is provided with. It is such that the outer loop selects an initial element and the inner loop goes through all elements in the array and constantly checks for the smallest element and exchanges it with the element selected by the outer loop. This ensures that the outer loop is only gone through once before the list/array is sorted as opposed to bubble sort which would often have the outer loop run multiple times (using a while loop) before the list/array is sorted. More often than not selection sort outperforms bubble sort.