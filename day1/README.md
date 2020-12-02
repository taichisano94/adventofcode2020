# Day1

## Part 1

### Brute Force

The very first idea that should pop up in your head is the brute force way. "Brute forcing" is to not consider efficiency of the algorithm and just have something that works.

Suppose `q1input` is a list of integers; we use a list here because it's the easiest data structure to visualize and work with.

```py
def brute_force(q1input):
  ## make a list here in case there are multiple solutions in the input
  solutions = list()
  for i in range(len(q1input)):
    for j in range(i+1, len(q1input)):
      ## we start at i+1 for j because 
      ## we don't want to do anything for when i = j
      if q1input[i] + q1input[j] == 2020:
        ## append the pair as a tuple so we won't accidentally
        ## mutate the data when we don't mean to
        solutions.append((q1input[i], q1input[j]))
  
  return solutions
```

_(In the code above, I intentionally left out the part where you multiply the two numbers together for the real answer. That part is trivial and not important to cover)_

This will get you the correct answer; you will find all the entries that when summed together will be `2020`. However, this is an `O(n^2)` algorithm which means you're searching the length of the list (in this case `q1input`) for every single element in the list (in the [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation), `n` in `O(n)` refers to the length of the input, typically an iterable).

The above `brute_force()` function would be considered a bad algorithm because it means as `n` grows, the time it takes for the algorithm to finish grows exponentially. So if length of `q1input` was 100 and it took the algorithm 10 seconds to finish, it will take 1,000 seconds if `q1input` was 10,000 elements long! (note: a list of 10,000 elements is considered very small in computer science; any "Big Data" problems typically work in the magnitude of hundred millions to hundred billions)

A short summary of what the Big O Notation is given by Wikipedia:

>In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.
>
>Big O notation characterizes functions according to their growth rates: different functions with the same growth rate may be represented using the same O notation.

Refer to this link for some common Big O Notation: <https://en.wikipedia.org/wiki/Big_O_notation#Orders_of_common_functions>

So `brute_force()` is not a very good solution; actually it's a really bad one. It works but if the input gets longer, the function will take longer (and worst case, never finish). What can we do to make this algorithm better?

### Picking apart the brute force

The main reason the brute force solution ends up being so inefficient is because of the data structure we use; a list.

A list is not very good for this problem because every time we want to look for a specific thing in the list, we have to check every element until we can find it. We would typically do something like this with code to find something:

```py
lst = [1, 2, 3, 4, 5]
if 5 in lst:
  print("I found it!")
```

When you do the above snippet, you are implicitly running the below logic:

```py
for i in lst:
  if i == 5:
    print("I found it!")
```

The above code snippet will run in `O(n)`. In the worst case, as in the snippet, we will have to look at every single element in the list to confirm if we found something or not. Although there are certain search algorithms that can sometimes be more efficient, the typical search efficiency of a list is `O(n)`.

Going back to the `brute_force()` implementation:

```py
for i in range(len(q1input)):
  for j in range(i+1, len(q1input)):
```

This nested `for` loop (a `for` loop inside a `for` loop) causes the `O(n^2)` run time. The outer `for` loop (`for i in range(len(q1input))`) will traverse through the entire list, which is `O(n)`. For each element in the list, we loop through the list again (`for j in range(i+1, len(q1input))`) which is another `O(n)`. Since we do an `O(n)` operation inside an `O(n)` operation, the result becomes `O(n) * O(n) = O(n^2)`. As it turns out, `O(n^2)` is one of the worst in efficiency; exponential growth is really poor performance and we really don't want the run time to grow that fast.

On the contrary, maps (or dictionaries in Python) and sets have a `O(1)` look up time ("look up time" is the effiency of finding an element in the data structure). `O(1)` means it takes a certain amount of time to do something and it is not affected by the length of the data structure; it will always take that unit of time. You will learn more about hash maps in a later class; for now just know that maps and sets are very efficient at knowing whether an element exists in itself or not.

What can we do so that we can use a dictionary or a set for a more efficient algorithm?

### Using faster look up

It turns out we can find the answer using a simple mathematical property.

```txt
x + y = 2020
```

The above can be rewritten as

```txt
y = 2020 - x
```

Using that to our advantage, we can use a set to write more efficient code.

Suppose `q1input` is a set of integers this time.

```py
def using_sets(q1input):
  ## make a list here in case there are multiple solutions in the input
  solutions = list()
  for x in q1input:
    y = 2020 - x
    if y in q1input and (y, x) not in q1input:
      ## we check that (y, x) is not in q1input so we don't have duplicate answers
      ## checking if a set contains something is O(1) so this operation is
      ## very minimal impact in the run time
      solutions.append((x, y))
  
  return solutions
```

The above will run in `O(n)` because we end up iterating over the entire input (`for x in q1input`) and checking if an element is in the set (`if y in q1input`) is `O(1)`. The final run time ends up being `O(n) * O(1) = O(n)`. 

That's much more efficient than the brute force method!

## Part 2

This time, we need to find 3 numbers instead of 2. We will have to make a twist on the previous approach.

If we do a brute force approach, we will have to add a third `for` loop and the run time will be `O(n^3)` - yikes!

We will take advantage of the fact that there is only one unique solution; there won't be multiple sets of 3 numbers that satisfy `x + y + z = 2020` (we know this because advent of code only allows you to input one answer).

We can do something similar to part 1 by treating two of the three numbers as a single number. We do this by first precalculating the sum of pairs and storing the result in a dictionary like so (`q1input1` is a set of `int`):

```py
def find_three(q1input):
  pairs = dict()
  for x in q1input:
    for y in q1input:
      if x != y:
        z = x + y
        if z not in pairs:
          pairs[z] = (x, y)

  ## we will implement the rest soon
```

The code so far is similar to the brute force method. Although the run time at this point is unfortunately `O(n^2)`, there isn't much we can do because we need to know every single pair's sum.

Once we know the sum of a pair of values, we can easily find the third to finish the function:

```py
def find_three(q1input):
  for x in q1input:
    for y in q1input:
      if x != y:
        z = 2020 - (x + y)
        if z in q1input:
          return (x, y, z)

  raise Exception("Input error: could not find 3 numbers that sum to 2020")
```

I decided to raise an exception so it's easier to see that the function found no answer. If that happened, I would know I have a bug in my code!

There might be an answer that is better than `O(n^2)` but I'm not going to pursue it.
