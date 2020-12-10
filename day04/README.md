# Day 4

## Part 1

There isn't much of a "gotcha" here; most of the effort comes from making sure that the file parsing is done correctly.

One thing to be wary of is that depending on how your input file ends, the `for line in f:` loop might end prematurely before the final passport information is appended to the list. Make sure to check that if any of the passport field information is not `None` after the loop exited, there is one more passport information to store.

We also use `None` as the default empty state for fields. This is better than using something like an empty string `""` or `0` because it's possible those two inputs are valid and also because we don't know what type to expect the input fields to be. Additionally, the entire point of the `Nonetype` is to express that the field is literally nothing. 

In terms of space efficiency, Python treats `None` as a singleton; there is only ever one single instance of `None` during run time. Meanwhile, multiple `""` can be created so if we use `""` to signify a field is empty, we end up allocating more memory to create multiple instances of `""`. This means that if we have multiple objects with multiple empty fields, setting those fields to `None` will save a lot of memory because all `None` points to a single space in memory while `""` will take up space for every one that is created.

A recurring theme of using classes to represent the information we want to store and manipulate. This makes your code much easier to read and extend, which we will see again in Part 2.

## Part 2

What we are asked to do is called "data validation" and it's typically done to make sure data we receive from a source is in a format we expect. Again, there aren't any obvious pitfalls to watch out for.

We would normally do data validation _before_ we allow the data to be passed into the object; data should be cleaned and prepared so by the time we store the data into class instances, we can operate on the assumption that the object is valid. For this particular problem, since the operation we are doing is validating the password, I baked it into the class itself.

We make the assumption that all fields passed into the class `Passport` are of type `str`. This lets us manipulate the `str` in convenient ways as you will see below.

The validations were done in the following:

* `birth year`, `issue year`, and `expiration year` work the same way; we first make sure that the fields are castable to `int`. If it's not, we should get a `TypeError` and the interpreter will throw an exception. We catch that exception and set the field to `None` which is our default "this field is bad or doesn't exist" state. If the field is castable to `int`, we check that the values are within acceptable range.
* `height` needs to always end in `cm` or `in` so we use string operation to check first if the field ends in either of those cases. If not, `height` is an invalid field. Otherwise, we take all characters in the field except for the last two (because at this point, they are guaranteed to be either `cm` or `in`) and attempt to cast the object into an `int`. If it fails, we know that the field was an invalid one (for example, `123bin` will result in us attempting to cast `123b` to an `int`). If it succeeds, we check that the value is within required range.
* `hair color` is expected to follow a very specific pattern in the string. Regex is an easy way to check for this. We use the regex `^#(\d|[a-f]){6}$` which broken down states:
    * `^#`: the string must begin with character `#`
    * `(\d|[a-f])`: next, we either expect a single digit (`\d`) (which is `0` thru `9`) or (`|`) a single character between `a` and `f` (`[a-f]`)
    * `{6}`: the above pattern needs to be repeated exactly 6 times
    * `$`: the string must end with the above pattern
* `eye color` always needs to be one of some specific values. We use a `set` to store those values beforehand and check if the value of the field is in the `set`. This is `O(1)` look up which is faster than using a `list`.
* `passport id` is easier to handle as a string first because if we convert the field to an `int`, we'll lose any information about leading zeroes (`000000001` will convert to just `1`). We first check that the length of the field is exactly 9 before we attempt to convert the field into an `int`. If the type conversion fails, that means the passport ID contained a non-digit character which invalidates the field.

One last thing to note is that `hair color` and `eye color` uses class attributes. This is another minor time/space optimization. Instead of creating the `set` and regex string every time the function is called for every instance of the `Passport` object, we do it once in the class definition and use it statically. Since these fields are always going to be the same for any `Passport` object, we avoid having to recreate the regex string and eye color `set` every time. While for this problem the optimization has minimal impact, it can be a big deal if the class attribute is a more complex object, the function is called many times, or if the class attribute is used many times.
