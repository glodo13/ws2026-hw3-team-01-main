# Defining the function
def prime_sum_to(number):

    # Input sanitization
    assert number >= 0

    # Initializing the result variable
    result = 0

    # Loop through all numbers from 2 to the given number
    for i in range(2, number + 1):
        is_prime = False

        # Checking if i is a prime number
        for j in range(2, i + 1):
            if i % j == 0 and i == j:
                is_prime = True
                break
            elif i % j == 0:
                break

        # Adding the prime number to the result
        if is_prime == True:
            result += i

    # Returning the result
    return result