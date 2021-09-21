# Python for ATC Lesson 1: Basic Python

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

## Hello World :wave:
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


## Variables & Operations
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

## Comments
- Use a `#` to mark the line as a comment.
- Comments have no affect on code output - they are there to help anyone reading the code to understand it.
For example:
```
a = 12
# This is a comment. This has no affect on the code.
b = 7 # Comments can also go in the same line as code.
```

## Data Types
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

## Strings vs Numbers
-  Strings represent a word or multiple words, or some sentences, or whatever.
- Numbers can only have a numerical value - no letters allowed
- The operations on each of these types are different

### String addition
- Operators like `+` have a different effect on strings than on numbers!
```
print('abc' + '123') # -> abc123
```
- For strings, addition **concatenates** them, that is, puts the strings together to form a single string.

# 
## :computer: Try Me!
- Can you figure out what the multiplication operator `*` does on strings? HINT: You need to multiply a string by a number.
#

## Casting Types
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