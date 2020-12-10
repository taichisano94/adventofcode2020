# Day 10

## Part 1

Since the adapters need to be within 3 jolts, working on a sorted list will make this problem easier. We first append 0 for the outlet and after the sorting, include the device adapter so that we don't forget to include them in our calculation.

We can then just use a simple sliding window and keep track of how many jolt-differences we saw.

## Part 2

This problem is actually a tricky and interesting to solve. The very first idea that comes to mind is the brute force way involving working from the beginning of the list and counting how many times we can reach the end, keeping track of every branching that happens. But the code will get complicated and there's a lot to keep track of. Should you use recursion to keep track of when there are multiple paths to take?

If you draw this problem out, you can notice a few things. The hint lies in the paragraph above: _branching_. What has branches? Trees, of course!

Using this as an example

```txt
16
10
15
5
1
11
7
19
6
12
4
```

First we sort the list:

```txt
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
```

Remember, we included the outlet and the device adapter to our list

As a tree:

![tree diagram of example](docs/advent2020day10.png)

_(you should draw this on pen and paper when solving this problem)_

When we draw it out, we can make several observations:

1. The number of 22 in the tree is the solution (8)
1. A lot of branches are actually the same
1. The total number of paths in a branch is the sum of paths of its children

We can go a few different ways here. From observation 1, we can create an algorithm that creates this tree as a data structure and count how many times we see the last adapter value. However, it's still complicated to make this data structure and furthermore, it seems inefficient to count all the branches after all the work we did so let's dig deeper.

Observation 2 is something we've done before; dynamic programming. If we calculate a branch, we probably should store the result the result so that we can just look up the result without having to recalculate it again.

Observation 3 is very interesting; if we take the node of value 7 as an example, you can see that the number of paths that we can take from 7 is actually the same number of paths we can take from node 10. And node 10 is the number of paths we can take from node 11 + number of paths we can take from node 12. Using that same logic, we can see that the number of paths we can take from node 4 is the sum of number of paths we can take from node 5, 6, and 7.

In pseudo-code, we can express this roughly like the following:

```py
## this keeps track of the number of paths for each node
path_counter = dict()

## we initialize this value first
path_counter[22] = 1

## there's only one node we can visit from node 19
path_counter[19] = path_counter[22] = 1

## likewise for these nodes
path_counter[16] = path_counter[19] = 1
path_counter[15] = path_counter[16] = 1
path_counter[12] = path_counter[15] = 1
path_counter[11] = path_counter[12] = 1

## node 10 can visit node 11 and 12
path_counter[10] = path_counter[11] + path_counter[12] = 1 + 1 = 2

## node 7 can only visit node 10
path_counter[7] = path_counter[10] = 2
## node 6 can only visit node 7
path_counter[6] = path_counter[7] = 2

## node 5 can visit node 6 and 7
path_counter[5] = path_counter[7] + path_counter[6] = 2 + 2 = 4

## node 4 can visit node 5, 6, and 7
path_counter[4] = path_counter[7] + path_counter[6] + path_counter[5] = 2 + 2 + 4 = 8

## finish the rest
path_counter[1] = path_counter[4] = 8
path_counter[0] = path_counter[1] = 8
```

It turns out if we work our way backwards up the tree and add the paths of the nodes that each node can visit (value within 3), we don't have to do any complicated branching and we can calculate it in `O(n)`.
