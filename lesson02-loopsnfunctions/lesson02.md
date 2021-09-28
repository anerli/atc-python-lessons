# Python for ATC Lesson 2: Loops and Functions and Stuff

## Overview
- `for` and `while` loops
- Functions
- File I/O
- Create a function for calculating the moving average of some data!

# Loops
- Loops repeat some section of code some number of times

## While Loops
- Executes the code below until the condition provided is not true

Example:
```
i = 1
while i < 10:
    print(i)
    i = i + 1
```
> Result: 1 2 3 4 5 6 7 8 9

---
## :computer: Try Me!
- Print all strings with only "a" of length 1 to 20, e.g. "a", "aa", "aaa", ...
- Hint: use either string concatenation or string multiplication
---


## For Loops
- For loops in python are used to **iterate** over all elements in an array, that is, store each one in a variable for use over a given code section.

Example:
```
my_items = ['thing1', 64, 'thing2', 'thing3', 12]

for item in my_items:
    print(items)
```

The `for <varname> in <arrayname>:` syntax allows you to visit all elements of `arrayname`, store them in the variable `varname` and then do whatever you want in the code block below.

> Note: The terms "array" and "list" are often used interchangeably in Python.

---
## :computer: Try Me!
- First, initialize some list of numbers
- Then, use a `for` loop to calculate the sum of all numbers in the list
---

# Functions
- Functions are a section of code that only run when **called**.
- The syntax for creating a function is `def <my_function_name>(<param1>, <param2>, ...):`

Example 1:
```
def print_hi():
    print('hi')

print_hi()
```
> Result: hi

Example 2:
```
def myprint(myparameter):
    print(myparameter)

myprint('hello')
```
> Result: hello

- The `return` keyword gives a value back out of the function which can be stored into some variable by the caller.

Example 3:
```
def add_numbers(x, y):
    return x + y

sum = add_numbers(3, 4)
print(sum)
```
> Result: 7

---
## :computer: Try Me!
- Write a function `make_triple` which takes 3 items, puts them in a list, and returns the list
---

# :warning: Under Construction
Hi the rest of this file is still being made

## File I/O

File I/O (Input / Output) is used when you want to read or write to files on the system the Python script is running on.

Example:
```

```