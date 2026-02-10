*This project has been created as part of the 42 curriculum by khhammou*

# Just python basics

To define a function in python

def function_name(parameter if needed here):

    code

input("Enter a number: ")

this prints to output the text inside and expects a string

casting the input to int casts result to an int value

print return None Always

int(input("Enter a digit: ")) prints it and asks for a digit

int(input(print("Enter a digit: "))) is incorrect since its like we 

are expecting a value that is a string prompt that we will cast to int

but the value passed to it in None since in python, the innermost call 

is evaluated first and could give errors

putting print("Total:", total)

The space after colon is added automatically by the comma

print() automatically converts numbers to string

so no need to cast to str like

total = (str)(day1 + day2 + day3)

build in functions in python should not be written:

like: sum, list, input, str

example:

numbers = [1, 2, 3]

print(sum(numbers)) # 6

If you do:

sum = day1 + day2 + day3 

python now thinks sum refers to your variable, not the built-in function

If later in program you try:

total_list = [1, 2, 3]

print(sum(total_list))

type error because sum is now an integer, not a function

print("total:", day1 + day2 + day3)

Everything is evaluated from left to right

argument by argument

first is the string "total"

then day1 + day2 + day3

python does the addition first

It automatically converts non-strings to strings when printing

It adds a space between arguments automatically

If theres signs they happen first

Only if you concatenate manually between a string and an int, you need str()

Example of concatenating:

1_print("Total: " + str(day1 + day2 + day3)) also works like the , but we need to add the space after colon here

2_print("Total: " + (day1 + day2 + day3)) Would give an error of only being ble to concatenate str not int so here is the only case we'd need the str cast

#CHECK flake8

python3 in terminal opens up the python interpreter

# def ft_count_harvest_iterative():
#     days = int(input("Days until harvest: "))
#     for i in range(1, days + 1):
#         print("Day", i)

#     print("Harvest time!")

The above code is another implementation of the count iterative approach

range(1, days + 1)

means the i will start with value = 1

and it will iterate while i < days + 1

so i goes from 1 to days (both included)

To make spaces the default again for python:

1_Ctrl+shift+p

2_preferences: open default settings JSON

3_add these lines

"editor.insertSpaces": true,

"editor.tabSize": 4,

"[python]": {

    "editor.insertSpaces": true,

    "editor.tabSize": 4

}

## Description

This python module is created to help the students build a basic 

understanding of some python practices such as if, else conditions,

using casting properly and using input() and some light recursion

### Instructions

To test the file, one can download the main.py provided in the subject 

and put it in the same path as each file that is going to be tested

and it runs all sorts of tests ad helps in debugging

One could also enter to each file directory, open a python interpreter and import the function and call it

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors