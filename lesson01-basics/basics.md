# Python for ATC Lesson 1: Basic Python

> More comprehensive information about various Python concepts is available on the internet, for example [w3schools](https://www.w3schools.com/python). This guide aims to be a beginner-friendly overview of basic Python concepts.

## Why Python?

- Easy to write compared to other languages
- Has good data science tools
- General purpose (versatile)

> We will use Python 3 not Python 2, because Python 2 is old and gross

## How do I use Python?

### Method 1 (Easiest):

Use repl.it - online interpreter so no installation required. Sign up and create a repl to start coding (Sign up -> create repl -> choose Python template -> write code & use run button to run code).

### Method 2:
Install [Python](python.org/downloads). Make sure to choose Python3. Running it will depend on your OS. If you check "ADD TO PATH" during installation, running it from command prompt / terminal will be a bit easier.

# Hello World :wave:
- Create a file called [hello_world.py](hello_world.py) (or anything ending in `.py`)
- Type in the following:

```
print('Hello ATC!')
```
- Run using your preferred method
- You should get the output:
```
Hello ATC!
```

# 
## :computer: Try Me!
- Modify the `'Hello ATC'` to print something else out!
#


# Variables & Operations
> Full Example Code: [variables.py](variables.py)
- Variables 'hold' data
- This data can come in many forms, for example numbers, letters/words (strings), and lists.

For example:
```
x = 5
y = 6
```
- Here we put the value 5 in x and the value 6 in y

If we print these out, we can see what they contain:

```
print(x)
```
> Result: 5

We can also do mathematical operations with number variables, e.g.:
```
z=x+y
print(z)
```
> Result: 11

Other primitive operations for numbers are `-` (subtraction), `*` (multiplication), `\` (division), `**` (exponentiation). Of course other mathematical operations exist and are accessible through the other modules (more on that later).

# Comments
- Use a `#` to mark the line as a comment.
- Comments have no affect on code output - they are there to help anyone reading the code to understand it.
For example:
```
a = 12
# This is a comment. This has no affect on the code.
b = 7 # Comments can also go in the same line as code.
```

# Data Types
> Full Example Code: [data_types.py](data_types.py)

The data types you will use most often in the python are strings and numbers.

Strings look like this:

```
my_string = 'ATC is my favorite club'
```
> Note: Both single quotes `'like this'` and double quotes `"like this"` function the same in Python.
> I like single quotes better, but it's all preference in Python.

Numbers are like the variables we defined in the previous example, e.g. `x=5`. Since these numbers are not wrapped in quotes, Python sees them as numbers and not strings. To see the difference:
```
i_am_a_number = 42
i_am_a_string = '42'
```

# Strings vs Numbers
-  Strings represent a word or multiple words, or some sentences, or whatever.
- Numbers can only have a numerical value - no letters allowed
- The operations on each of these types are different

## String addition
- Operators like `+` have a different effect on strings than on numbers!
```
print('abc' + '123') # -> abc123
```
- For strings, addition **concatenates** them, that is, puts the strings together to form a single string.

# 
## :computer: Try Me!
- Can you figure out what the multiplication operator `*` does on strings? HINT: You need to multiply a string by a number.
#

# Casting Types
- What if I have a number stored as a string, e.g. `x='123'`, but  I want x to be a number not a string?
- We can **cast** x to a number type.

```
x = int(x) # Set x to be itself but cast as an integer
```

> Note (int / float): Numbers actually come in two main types, whole numbers (integers - int) and numbers with decimal points (floating point - float). Cast to the corresponding one depending on if you need decimals or not.

We can use a similar string cast to convert numbers to strings:

```
string_x = str(x)
```

When something is an integer, we can do number things with it, e.g.
```
print(int('1') + 1) # -> 2
```

Similarly, when we cast something to a string, we can use string operations:
```
print('1' + str(1)) # -> '11'
```

# Booleans
> Example Code: [booleans.py](booleans.py)
- A Boolean is a variable type that can either be True or False.
For example:
```
a = True
b = False
```
> Note: Capitalization matters! `True` is a boolean primitive, while `true` means nothing at all!

We can check if booleans are True with an `if` statement:
```
if a:
    print('a is True!')
```
- If the expression after the `if` (in this case, `a`) evaluates to true, the following code block executes.

> Note: Indentation defines control flow in Python. Without a tab after the if statement, the syntax would be incorrect and the interpreter would give an error.

We can also form boolean expressions by combining numbers with comparison operators (==, <, >, <=, >=).

```
if 10 < 20:
    print('10 is less than 20!')

if 1 == 2:
    print('1 is equal to 2!') # This line will not execute, because 1 == 2 is false.
```

We can also incorporate the keyword `else` to do something when the `if` statement is False

```
if 2 <= 1:
    print('2 is less than or equal to 1')
else:
    print('2 is not less than or equal to 1')
```

Finally, we can combine the logical operators `and`, `or` to combine boolean expressions:
```
if True or False:
    print('cool')
    # Code here executes
```

# 
## :computer: Try Me!
- Try some conditionals!
- Define some integer variables and some boolean variables.
- Combine them in weird ways with comparison operators and logical operators and see if you can guess if the `if` statement will execute or not.

E.g.
```
x = True
y = 2 > 3
if ('a'=='a' or 1==2 and x) and ((1 < 2 and 123==123) or y):
    print('this executed??')
```
#

# Lists
> Example Code: [lists.py](lists.py)
- Lists are good for storing a bunch of things together in order, whether that be some numbers, some strings, or perhaps you want a list with more lists inside it!
- We use brackets `[` `]` to denote a list and commas to separate elements of the list.

Example:
```
my_list = ['a', 'b', 'c', 1, 2, 3]
```

We can print out the contents of a list by just printing out the variable.

```
print(my_list) # -> ['a', 'b', 'c', 1, 2, 3]
```

## Indexing
- We can **index** at a particular point in a list to access the value at that position in the list. Indices start with zero. In this case the index 0 refers to the value 'a', the index 1 refers to the value 'b', ..., index 5 refers to value 3.
- We access these items using the syntax `list[i]` where list is the list variable and i is the index we want the value at.

For example:
```
print(my_list[2]) # -> c
```

We can also change the value at a certain point, for example:
```
my_list[2] = 'potato'
print(my_list) # -> ['a', 'b', 'potato', 1, 2, 3]
```

We can add new elements to the end of a list using the `append` function:
```
my_list.append('tomato')
print(my_list) # -> ['a', 'b', 'potato', 1, 2, 3, 'tomato']
```

# Input
- Here is how to get text input from the user running your program from the terminal:
```
thing = input('Give me a thing please: ')
print(thing)
```

#
## :computer: :warning: :non-potable_water: Challenge Round!! :biohazard: :radioactive: :do_not_litter:
- Create a program which does the following:
- Initialize (store in a variable) a list of some made up stock prices, for example `[10.2, 11.3, 11.6, 12.0, 13.6, 15.12, 14.2, 11.8]`
- Determine how much profit a buy-and-hold strategy would make if you bought one hundred stocks at the beginning of this made-up period and sold all one hundred and the end of this period. (Hint: If you don't feel like counting to get the last element of the list, you can use the index `-1` to get the last element).
- Store this profit value in some variable.
- Print it out with some text describing what it is, e.g. `Profit: $x.xx`.
- Ask for help if you can't figure it out!
- BONUS: Instead of simulating buying and selling 100 stocks, calculate the profit with `n` stocks, where `n` is some input number you collect from the user using the `input()` function.
#