# Sorting algorithms
Searching in an **unsorted array** takes  **O(n)** times,he worst case, the algorithm must iterate through every element (Linear Search). In a sorted array, the same operation takes **O(log n)** using an Algorithm called [**Binary Search**](BinarySeach.md). This approach repeatedly divides the search interval in half, significantly reducing the number of comparisons.

A collection of elements can be arranged in a specific order, (e.g., numbers in ascending/descending order or strings in alophabetic order). Sorting algorithms are generally categorized by their time complexity.

* **Cuadratic O($n^2$)**: There are intuitive and easy to implement, but become significantly slower as the input increases. They are typically only recommended for small datasets or educational purposes.
    * Bubble Sort
    * Insertion Sort
    * Selection Sort
* **Log-linear O($n \log(n)$)**: These utilize a Divide and Conquer strategy, often through recursion, to achieve much higher efficiency. They are the standard for production-level applications dealing with large amounts of data.
    * Merge Sort
    * Quick Sort