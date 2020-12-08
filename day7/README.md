# Day 7

## Part 1

For this problem, we use a mixture of [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) and [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)). Dynamic programming is a fancy way to say "reuse the answer we already calculated before".

In this problem, we want to store the answer to whether a bag can contain a shiny bag or not after we've calculated it once. For example, if we calculate that `bright white bag` contains `1 shiny gold bag`, we store a boolean that says "`bright white bag` can contain `shiny gold bag`". When we want to calculate later whether a `light red bag` can contain `shiny gold bag`, we see that a `light red bag` contains a `bright white bag`. We then check to see if we've already calculated `bright white bag` before; we have! We don't have to recalculate what kind of bags `bright white bag` contains; we already calculated and stored a boolean from before that `bright white bag` _can_ hold `shiny gold bag`.

We use recursion to continuously check down the bags and the bags inside the bags to see if it can contain `shiny gold bag`. Inside the recursive function, we can also update every bag we checked on each step whenever we know whether the bag can contain a `shiny gold bag` or not.

We use nested dictionaries in this problem because we want to constantly check a bag type and its subsequent policies regarding it. The `O(1)` look up time makes dictionaries a perfect use case for this.

## Part 2

We can use the identical approach, this time instead of checking booleans, we keep count of the quantity. Don't forget the inside bag itself as a single bag; we keep track of this code by adding an additional `quantity` to the bag count.

Note that in both Part 1 and Part 2, the recursive function is prefixed with `_`. In Python, [private functions](https://stackoverflow.com/questions/1020749/what-are-public-private-and-protected-in-object-oriented-programming) aren't natively supported. It is convention to prepend any function that shouldn't be accessed by anything other than itself with `_`. In this case, it doesn't make sense for something other than `BagPolicy` to use a recursive function. Recursive functions can only be used for specific cases so only the class `BagPolicy` itself should have control over when such function should be used.
