# Importing the relevant modules and functions
from business import *
from conversion import *
from geometry import *
from polynomials import *
from prime_addition import *
from rot13 import *
from vrptw_reader import *


def main():

    # Initializing the controll value
    controll_value = 0

    # Setting up the test cases
    tests = [
        # Task 1
        (eval_polynomial, ([1, 2, 3, 4, 5, 6, 7], 2), 769),

        # Task 2
        (prime_sum_to, (10,), 17),
        (prime_sum_to, (100,), 1060),

        # Task 3
        
    ]

    # Running the test cases and checking if the actual output matches the expected output
    for function, arguments, expected in tests:
        actual = function(*arguments)
        print(f'{function.__name__}{arguments}; expected: {expected}, actual: {actual}')
        if actual != expected:
            controll_value = 1

    # Returning the controll value
    return controll_value