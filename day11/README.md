# Day 11

## Part 1

This problem isn't particularly tricky but rather tedious and requires attention to detail. It's very important in this problem to make sure your code stays organized and easy to read to help you understand your own code. It's easy to get caught up in the details in problems like these and get confused in your own code as you try to debug.

The first thing I did was to create a class for `Seating` because I realized the seating is going to have some complicated properties and would benefit from having helper functions. In particular, overriding the equality operator to be able to compare whether two instances of `Seating` were the same helped make the code a lot simpler. I also overrode the string operator so that I can visually see what I was doing to the seating chart with each iteration. It's important to make yourself tools to help you better understand the problem and see what's going on in your data structures.

I also broke down the problem into several parts and worked on them in order:

1. Determine a data structure to express the seating chart. This needs to be easy to iterate since we need to go over each seat
1. Be able to obtain adjacent seats given a row and column index
1. Decide on a useful data structure to express these adjacent seats
1. Be able to iterate over every seat and obtain the seat's adjacent seats
1. Using the adjacent seats, determine what the new state of the seat is
1. Create a new seating chart based on new information gathered by repeating step 5 on each seat
1. Determine how to evaluate whether seating state changed between iteration

On each step, I stopped to make sure that the step worked as expected before I moved onto the next. By doing this, I make sure that when something goes wrong, I have a better idea where to look for the bug. A bug is most likely present on the code related to the step I'm working on because I have more confidence that the previous steps works.

I also created an `enum`-like class for the types of seat that's possible. This makes the code easier to read than hardcoding the string value of the seat types.

### Step 1

This is most likely always going to be a list. In my case, I used a list of strings with each string representing a row of seats. Strings are iterable in Python so there's no need to break the string into a list.

### Step 2

If we treat the list of strings as a grid (or a matrix) with `(0,0)` starting at the top left, adjacent seats are determined by manipulating the `x` and `y` values for any given seat. We treat the rows as the x-axis and the columns as the y-axis. Diagonal up left adjacent seat is moving up one row (subtract 1 from the `x` value) and left one column (subtract 1 from the `y` value), up adjacent seat is moving up one row (subtract 1 from the `x` value), and so on and so forth. We use `None` as the default state to differentiate the floor with being out of bounds. We need to be mindful not to bump into `IndexOutOfBounds` errors.

### Step 3

I decided to go with a tuple because I want the adjacent values to be immutable and iterable. We worked so hard to obtain them, we don't want to accidentally introduce a bug by unknowingly mutating them! We need the adjacent values to be iterable because we want to count the number of seat types later.

### Step 4

We set up the nested `for` loop so we can go over every list. We take care to name these variables something understandable so that we don't confuse ourselves in the code. `row` is referencing the row of seats and `seat` is a single character in the `row` that symbolizes a single seat.

### Step 5

We can use the neat `count` function on the tuples to determine how many types of seat is in the adjacent seats we found.

### Step 6

We need to create an entirely new seating chart as the state changes because we can't edit the seating chart until all seats have been processed. The key word is that the seats get occupied or emptied _simultaneously_. Only at the very end after every seat has been processed can we change the seating chart to the next state. In order to preserve the seating chart until the end, we need to make a new list and keep track of the changes separately.

### Step 7

I decided to return a new instance of `Seating` with the new seating chart state instead of editing the existing `Seating` object. If I do that, I have access to both the new state and the old state and makes it a lot easier to compare if the states changed. This is why I decided to override the equality operator for the `Seating` class.

When we put all the steps together, we get the class `Seating` that's able to update its state one iteration at a time. I wanted the `Seating` class to only handle one iteration at a time so that I can `print` each iteration and make sure the seat chart is being updated correctly. We can always automate the iteration at the end with a `for` loop.

## Part 2

This problem is actually very similar in approach, just that we need to update how we retrieve adjacent seats. Actually "adjacent seat" is no longer correct since we care about seats that are within line of sight instead.

Line of sight is easy to express if we treat the seat chart as a grid again. The non-diagonal directions are simple; they move along the `x` or `y` axis in either direction. The diagonals move in a straight linear line with a slope of 1 or -1.

Because we made our code modular, the function that takes care of determining how seat states change isn't affected very much by this change. As long as we can supply the correct "adjacent" seats, the function can do its job. We can almost use the function like-for-like with minor modifications.
