# CMS2 - HW3 - Functions

This homework is the first homework to be solved in teams of two using team programming. Currently, the number of roastered students is odd. Thus, we can have one team with three members, or one of you volunteers to work alone. Since you work on one team-repositoriy, you need to maintain only one. However, this can be a tricky task if done for the first time, because you can easily produce conflicts if you work only in the master branch. A tyically workflow is to create branches in the repository (one for each team member), and to merge them into the master branch. This way you can resolve conflicts before you push the work into the master branch. Other options include:
- to use the [live share feature](https://docs.github.com/en/codespaces/developing-in-a-codespace/working-collaboratively-in-a-codespace) of codespaces,
- to distribute work such only one person works at a specific file,
- to work asynchronous.
If you do not work in branches, keep in mind that each time you start to work, you should pull the current state of you repository, because a team-member might already did some changes (which you do not see one your local clone unless you pull the last state).

Note that the grader will not work unless you created all files.

If you need to load files from disk, please change the path of the current working directory to the one where your file (and script file) is located as follows.
```
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
```

## 1. Polynomial evalution
Write a function `eval_polynomial(coefficients, x)` that evaluates the polynomial given by the coefficients. Note that `coefficients` is a list of numbers, `coefficients[i]` ($c_i$) is the coefficient of $x^i$, whereas `x` is number. For instance, if there exist four coefficients, the function should evaluate the polynomial:

$c_0 x^0 + c_1 x^1 + c_2 x^2 + c_3 x^3$

and return the result. Name the program file: `polynomials.py`

## 2. Prime Sum
Write a function `prime_sum_to(num)` that takes an integer `num >= 0` as sole argument. The function should return the sum of all prime numbers `<= num`. In the function, assert that the input is `≥ 0` by using `assert`.

Name the program file: `prime_addition.py`


## 3. Conversion between Celsius and Fahrenheit
Based on the formulas and your code of the first homework, write a function `celsius2fahrenheit(.)` that converts from Celsius to Fahrenheit and `fahrenheit2celsius(.)` for the other way around.
    
Name the program file: `conversion.py`

## 4. Geometry functions
Implement the following functions calculating the perimeters, areas, surfaces or volumes of common gemoetric shapes:
```
perimeter_right_triangle(c1, c2)
area_right_triangle(c1, c2)
perimeter_circle(r)
area_circle(r)
surface_sphere(r)
volume_sphere(r)
surface_cylinder(r, h)
volume_cylinder(r, h)
surface_cone(r, h)
volume_cone(r, h)
```
Name the program file: `geometry.py`


## 5. Business functions
Implement a function `interest(capital, rate, years=1, tax=0)` that returns the profit (compound interest) of investing money. If a positive tax value is entered, every year's interest is to be reduced by the tax. The `rate` and `tax` parameters must be between 0 (0%) and 1 (100%). The number of years is integral.
Using the above function, implement a second function that returns the terminal value of investing money: `terminal_value(capital, rate, years=1, tax=0)`.

Name the program file: `business.py`
    
    
## 6. ROT13
Building on your solution to the ROT13 task in the last homework, write a function `encode(.)` that takes a string and returns the given string rotated by 13 places. For symmetry, also provide a corresponding `decode(.)` function. Convert the input to upper case before performing the rotation.
```
a. Arire gehfg n cebtenz lbh qba'g unir fbheprf sbe.
```
Name the program file: `rot13.py`

    
## 7. VRPTW instances
Write a function `read_string_list(.)` that opens a problem instance file of the vehicle routing problem with time windows (VRPTW) given as filename argument. The argument must be optional and default to "r101"). If the argument doesn't contain a filename extension (".txt"), this extension must be added before opening the file. Your function should return a list of strings - one for each entry. The headers should not be included in that list.
A sample execution of this function:
```
>>> read_string_list('r101.txt')
['    1      35.00      35.00       0.00       0.00     230.00       0.00\n',
 '    2      41.00      49.00      10.00     161.00     171.00      10.00\n',
...
 '  100      20.00      26.00       9.00      83.00      93.00      10.00\n',
 '  101      18.00      18.00      17.00     185.00     195.00      10.00\n']
```     
Name the program file: `vrptw_reader.py`


## 8. More on VRPTW instances
Expand the file  `vrptw_reader.py` of the last task to include more functions. The second function `get_demand(.)` takes two arguments. The first argument should be a list of strings (one for each entry) and the second should be a customer number (CUST_NO.). The function has to return that customer's demand as floating point number. The last function, `calc_distance(.)`, should take three parameters – a list of strings and two customer numbers. It should return the euclidean distance between the two customers.


## 9. Main function
Write a single module that imports all the other modules you wrote for this homework. In the module implement a main function that uses all the functions you created (except function `read_string_list(.)`). This main function is a first attempt of testing your code in the other modules. For each of the other tasks, create valid input data and deduce the functions output. Print these values, followed by the actual values the function produces for these inputs. Here's an example line this function could contain:
```
def main():
    # ...
    print('prime_addition.prime_sum_to(9); expected: 17, actual:',
          prime_addition.prime_sum_to(9))
    # ...
```
The main function must be called itself using the ifmain pattern. If all went well, the main function must return 0 to inform the calling process of the successful termination. 

Name the program file: `main.py`
