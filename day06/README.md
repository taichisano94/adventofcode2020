# Day 6

## Part 1

The first data structure that springs to mind after you read the prompt should be `set`. This is the perfect use case for using sets; we don't care about duplicates and we want to guarantee uniqueness.

The implementation is simple. For each series of answers we receive, we put each character in a set. If anyone else answers the same questions, the set will ignore the duplicates. If anyone answers a different question, the set will take the unique element. In the end, we have a set with all unique answers.

## Part 2

Sets are still perfect data structure to use here. We can use the `intersection()` method of sets to only keep overlapping answers. Whenever an intersection is impossible between two answers in a group (any scenario where two different answers have no common characters), we can just throw out the entire group.

There aren't any particularly tricky pitfalls here.
