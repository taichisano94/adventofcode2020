# Day 3

## Part 1

The tricky part of this problem is how to deal with the repeating pattern of the rows. Consider the slope pattern in the example:

```txt
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

The length of characters on each row is 11 meaning if we travel right 12 times, we'd run out of characters. More precisely:

```py
right_counter = 0
for line in slopes:
  right_counter += 3
  print(line[right_counter]) ## <-- this will get an IndexError eventually
```

To get around this, we can follow the instructions literally:

> These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

```py
right_counter = 0
for line in slopes:
  right_counter += 3
  while right_counter > len(line):
    ## double the amount of times we repeat the line until we have enough length
    line = line * 2
  print(line[right_counter])
```

However, this isn't very space efficient. If we consider the secnario that we need to process a file with 1 billion lines, `right_counter` is going to get huge and by the end, we'll have to store strings that are billions of characters long.

A more efficient way is to take the modulo of `right_counter` by the length of the line. This will give us the correct index as if the pattern continues forever without actually having to take up space.

If we go back to the first example (`!` denotes where `line[right_counter % len(line)]` would be in the list):

```txt
!.##....... right_counter % len(line) = 0 % 11 = 0 <-- use as index of the line
#..!#...#.. right_counter % len(line) = 3 % 11 = 3
.#....!..#. 6 % 11 = 6
..#.#...#!# 9 % 11 = 9
.!...##..#. 12 % 11 = 1
..#.!#..... 15 % 11 = 4
.#.#.#.!..# 18 % 11 = 7
.#........! 21 % 11 = 10
#.!#...#... 24 % 11 = 2
#...#!....# 27 % 11 = 5
.#..#...!.# 30 % 11 = 8
```

At that point, we just need to check whether the character in the line at that index is an open space (`.`) or a tree (`#`).

## Part 2

This worked out very nicely for me since I decided to make a class that's reusable. I simply add more `for` loops for each of the scenarios to test and get the answer.
