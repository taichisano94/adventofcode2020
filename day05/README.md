# Day 5

## Part 1

There are two ways to do this problem. One way is more involved than the other. We'll cover both ways.

### The Involved Way

The involved way is mostly following the requirements as written. The first step is recognizing that there are two parts to the given boarding pass code; the part that calculates the rows and the part that calculates columns. If we look closely, we can see that although the characters are different, they both do the same thing.

The algorithm involves squeezing the lower and upper bounds of the interger range until you have one option left. This is called [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm). We will go through the columns as an example of how it works.

In binary search, the prerequisite is that we are working on a sorted list. In this problem's case, the column is a list of seats with unique numbers on them.

Here is an example of how the algorithm will work with the code `RLR` (`l` means _lower bound_ while `u` means _upper bound_):

```txt
0. We start with the entire list with the lower and upper bound set
   at each end of the list

l             u
0 1 2 3 4 5 6 7

1. We first work on the first R, which means "take the upper half". 
   We split the  list in half and ignore the lower half of it

        l     u
0 1 2 3 4 5 6 7

2. Next is L, which means "take the lower half".
   We split the portion of the list we care about (between l and u which is 4~7)
   in half and adjust the bounds accordingly.

        l u
0 1 2 3 4 5 6 7

3. Next is R, which means "take the upper half".
   There are no items between l and u so we take the higher of the two.

0 1 2 3 4 5 6 7
          ^

We found 5!
```

The same can be done for `FBFBBFF` but with 0 thru 128 instead.

The code for this implementation can be found in `BoardingPass.calculate_binary_search()`.

### The Less Involved Way

The alternate way is to recognize that this is actually a problem involving binary numbers.

In binary, we use only two states; `0` for `False` and `1` for `True`. This is where the [power button icon](https://en.wikipedia.org/wiki/Power_symbol) comes from; `O` stands for `0` (`False`, or `Off`) while `I` stands for `1` (`True`, or `On`). At the very lowest of levels, computers work with just these two states and use logic gates to express more complex things.

To express integers, bits are used. Starting from 0:

| Binary  | Integer|
|---------|--------|
| 00000000| 0      |
| 00000001| 1      |
| 00000010| 2      |
| 00000011| 3      |
| 11111111|127     |

The math works like this:

```txt
Given a binary 1001001

(1 * 2**6) + (0 * 2**5) + (0 * 2**4) + (1 * 2**3) + (0 * 2**2) + (0 * 2**1) + (1 * 2**0)
= 64 + 0 + 0 + 8 + 0 + 0 + 1
= 73
```

We can then apply this logic to the boarding pass. Since `F` and `L` means to take the lower half, we will treat them as `0` and `B` and `R` as `1`.

If we use `FBFBBFF` as an example, we can substitute the characters for their appropriate bit values to get the binary string `0101100`. If we calculate this binary to an integer:

```txt
0101100 ->
(0 * 2**6) + (1 * 2**5) + (0 * 2**4) + (1 * 2**3) + (1 * 2**2) + (0 * 2**1) + (0 * 2**0)
= 0 + 32 + 0 + 8 + 4 + 0 + 0
= 44
```

Treating the problem as binary numbers make the code much simpler. The implementation can be found in `BoardingPass.calculate_binary()`.

## Part 2

There isn't a lot of trickery here. The brute force method is to line up all the seats in a list by ID and sort them. After that, we just look at each item and see if a seat has +1 and -1. If there is a spot missing, that is the open seat we are looking for.

There might be some optimizations here but the biggest bottleneck here is the sorting, which might be anywhere from `O(nlogn)` to `O(n^2)`. We leveraged Python's sorting algorithm so we can trust that it's not awful so it should be fine.

Let me know if you found a more clever solution :)
