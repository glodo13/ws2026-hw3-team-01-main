# Defining the function
def eval_polynomial(coefficients, x):

    # Computing the polynomial value using a loop
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** i)

    # Returning the result
    return result