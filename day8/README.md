# Day 8

## Part 1

This problem does not have a lot of pitfalls or optimizations either. Make sure that your code works on the provided examples before working on the main input file; it will save you a lot of hair pulling by making sure your code works on a simple example before debugging a more complicated one. If you encounter a bug in your code, be sure to use the debugger as well.

Because there aren't a lot of interesting things to talk about in terms of problem solving, we will discuss how to write neater code instead. These are mostly my opinions so don't treat these as gospels; you should trust your gut on what is readable and maintainable code.

The first thing to be mindful in this problem is to name your variables properly. It can get easily confusing if you have poorly named variables. For example, I made sure to distinguish what the variables `line` and `position` meant in the context of my code. `line` can be particularly confusing; it can potentially point to the current line of instructions that's being ran or the line number of the instruction. I made sure to never use those two terminologies interchangeably within my bode. `position` should always mean line number and `line` should always reference the line of instructions itself.

Another thing I did to organize my code was to create an [enum](https://en.wikipedia.org/wiki/Enumerated_type) for the operation code. Python doesn't explicitly support enums so I created a sort of psuedo-enums using a class and class attribute. Enums are handy to use with operation code because they are constant values that express a certain idea. Compare the following code snippets:

```py
## without enums
if operation == "nop":
  do_nop_stuff()
elif operation == "jmp":
  do_jmp_stuff()
elif operation == "acc":
  do_acc_stuff()

## with enum
if operation == OperationCode.NOP:
  do_nop_stuff()
elif operation == OperationCode.JMP:
  do_jmp_stuff()
elif operation == OperationCode.ACC:
  do_acc_stuff()
```

At first glance, the enum code is easier to understand; it's instantly discernible that `operation` is referencing an idea called `OperationCode`. And what if you used the non-enum code in many places and suddenly you find out you misspelled `acc`? The enum keeps your code tidy by having a singular place to manage that information. It reduces copy/paste and repeating code.

I also purposely use tuples to store each line of instructions. I leverage tuple's property of being immutable after creation so that I don't edit the instructions in my code. This prevents bugs involving me unknowingly changing the instructions.

## Part 2

We _could_ manually edit the input text file one by one until we find the answer we need. Or we can create a helper function to run all the simulation for us. The former sounds tedious and error-prone (we don't trust humans to accurately do mundane, repetitive tasks). We're programmers, we're going to make the computer do it!

Remember that Python passes by reference. This means that if we modify the parameter inside a function, the object itself gets modified. When we run simulations by swapping operaton codes, we need be mindful that original instruciton set will get modified. There are two ways to go about this: make the change and run the simulation and swap it back to original or make a copy of the original instructions and only apply modifications to the copy. I decided to go with the latter because it's easier to make a copy and throw the copy away afterwards than keep track of changes I make to the original.

I use Python's built-in `copy` library to make a shallow copy. I only need a shallow copy because the objects stored inside the `instructions` list are tuples; there aren't any concerns about the inside objects being modified and causing a bug (tuples are immutable so I can't modify them anyway). [Learn more about shallow copy and deep copies.](https://docs.python.org/3/library/copy.html)
