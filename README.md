# lisp_interpreter
Lisp interpreter written in Python.

It's not full intepreter, but it can do some fun stuff with it.

## How to run
To run just write:

`python3 main.py`


## Functionalities

### Basic operations/arithemtics

You can perform basic operations e.g. `(+ 1 (- 4 5))`

(only for two arguments for the operator).

You can define you variables, e.g. `(defvar a 10)` - it will assign 10 to a.

If you want to change the value - `(set a new_value)`

And then print them - `(print a)`


### Conditionals

Syntax:

`if var consequence alternative`

e.g.:

`(if (equal a 10) (print a) (print (+ a 1)))`

If you want to check equality between to variables, write `equal`. Other operators are normal: `>, >=, ... `

### Lists

Create a list: `(list a b c)`
Get en element of a list: `(getl listname index)`
Add en element to a list: `(append listname element)`
set an element on a position: `(setl listname index element)`


### Functions

You can also define your own functions:

`(deffun funname (args) (body) )`

For example:

`(deffun double_x (x) (* x 2))`

or

`(deffun sum_till_0 (x) (  if (> x 0) (+ x (sum_till_0 ((- x 1))) ) 0 ))`