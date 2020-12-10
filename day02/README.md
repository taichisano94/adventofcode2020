# Day 2

## Part 1

Before we begin, we start by pointing out some characteristics of the problem:

* We only care about a single letter for each password policy; we don't care about any of the other letters in the password
* We need a way to keep count of how many times a letter occurred in a password

We can then divide the problem into two parts:

1. Be able to read the input file and extract the information in a way we can use it
2. Determine if each password is valid based on its policy

I decided to create a class to represent the password policy because it's an easy way to represent data and I was wary that I may have to add more features to the password policy in part 2. You could also do this with functions without using classes as well.

For my class, I allowed the `password` field to be `None` and optionally supplied; for most use cases, this should be supplied according to the input field but I wanted to be able to test the policy against random other passwords in case I need to debug.

## Part 2

It seems it was a good idea to store the password policies in a class because I need to reuse the same information again, just in a different way.

I can easily add a new method to my `PasswordPolicy` class that adheres to the new requirements.

In this case, I use the logical `xor` because the password is only valid if one of the positions is the character but not both.

For `xor`:

```txt
True ^ True = False
True ^ False = True
False ^ True = True
False ^ False = False
```

which is exactly what we need.
