# Day 9

## Part 1

To solve this problem, we create a [sliding window](https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples) to account for adjacent elements in the list. Similar to Day 1's problem, we use the nice property of math that `x + y = z` is the same as `y = z - x`. We create a `set` out of the window and check if the pair exists in the window for each element in the window. If such a pair exists, then the property of the XMAS data upholds. We continue to slide the window until we find such an element in the list where a pair does not exist.

Remember that we should use a `set` here because we are checking whether an element is in the `set` or not. For a `set`, this operation is `O(1)` while if we use a list, it becomes `O(n)` (the list has to check every element inside to determine if something is in the list).

## Part 2

This part can be solved in a similar way but we have to modify the window a little bit. We take advantage of the fact that the elements must be contiguous. Every time the sum of the elements in the window is smaller than the target sum, we increase the window by 1. If it's larger, we decrease the window size by 1. The window shrinks and expands as it makes its way down the list until it finds the contiguous sequence of elements that totals the target sum.

To illustrate the algorithm:

```txt
We start with 

35 20 15 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

and we look for a contiguous window whose sum totals 127.

1. 
Window size = 1
Window sum = 35 < 127
[35] 20 15 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Increase window size by 1

2.
Window size = 2
Window sum = 55 < 127
[35 20] 15 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Increase window size by 1

3.
Window size = 3
Window sum = 70 < 127
[35 20 15] 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Increase window size by 1

4.
Window size = 4
Window sum = 95 < 127
[35 20 15 25] 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Increase window size by 1

5.
Window size = 5
Window sum = 142 > 127
[35 20 15 25 47] 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Decrease window size by 1

6.
Window size = 4
Window sum = 107 < 127
35 [20 15 25 47] 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Increase window size by 1

7.
Window size = 5
Window sum = 147 > 127
35 [20 15 25 47 40] 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Decrease window size by 1

8.
Window size = 4
Window sum = 127 = 127
35 20 [15 25 47 40] 62 55 65 95 102 117 150 182 127 219 299 277 309 576

Window found!
```
