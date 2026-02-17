# Arrays
An array is a contiguous block of memory that stores a collection of elements.
* **Statically Typed Languages (e.g., C):** All elements must share the same data type. The compiler reserves a specific amount of memory based on the type (int, char, float, etc.) and the number of elements. Because each element occupies a fixed-size slot, the system can calculate the exact memory address of any index.
```C
int arr[10] = {1,2,3,4,5,6,7,8,9,10} //10 is the size of the array

```
* **Dynamic Languages (e.g., Python):** These do not store the literal data directly within the array's contiguous space. Instead, they store references (pointers) to objects located elsewhere in memory. This removes the limitation of uniform types, allowing a single array to contain integers, strings, or any other object.
```python
li = [1,"Hola", 123.976] #there is no need to specify the size of the array.
```
The easiest way of accessing a particular element in the array is through its index. For a given array of length 10 ```n = 10```, their indices go from 0 to 9 (```n-1```).
* ```arr[0] //1```
* ```li[1] #Hola```
* ```arr[9] //10```

In both type os languages, an array is static, which means it has a fixed-size.

> [!NOTE]
> In Python, when an array/list is defined, the Python Interpreter over-allocates memory by reserving extra space.
> * Efficiency: Typically, this "extra room" allows for appending elements on the fly without needing to request more memory from the OS every single time.
> Dynamic Resizing: However, once the reserved memory block is completely full and a new append operation is performed, a larger block of memory is allocated. The existing elements are then copied to this new location, and the new value is added.

