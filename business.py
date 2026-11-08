# Function for calculating the interest earned after taxes
def interest(capital, rate, years=1, tax=0):

    # Input sanitization
    assert 0 <= rate <= 1, "The interest rate must be between 0 and 1."
    assert 0 <= tax <= 1, "The tax rate must be between 0 and 1."
    assert isinstance(years, int), "Years must be an integer."

    # Initializing the result variable
    compounded_interest = 0

    # Calculation of the result with a loop
    for i in range(years):
        interest_after_tax = capital * rate * (1 - tax)
        capital += interest_after_tax
        compounded_interest += interest_after_tax
    
    # Returning the result
    return compounded_interest

# Function for calculating the terminal value
def terminal_value(capital, rate, years=1, tax=0):
    return capital + interest(capital, rate, years, tax)