
def read_string_list(filename="r101"):
    # Step 1: Add the ".txt" extension if it is missing
    if not filename.endswith(".txt"):
        filename += ".txt"

    # Step 2: Open the file in read mode(r)
    with open(filename, "r") as file:
        # Step 3: Read all lines from the file
        lines = file.readlines()

    # Step 4: Create an empty list to store customer data
    string_list = []

    # Step 5: Iterate through each line in the file
    for line in lines:
        # Step 6: Remove surrounding whitespace for checking
        stripped_line = line.strip()

        # Step 7: Skip empty lines and header lines
        if not stripped_line:
            continue

        # Step 8: Split the line into individual values
        values = stripped_line.split()

        # Step 9: Check whether the line contains seven values
        # and whether the first value is a customer ID
        if len(values) == 7 and values[0].isdigit():
            # Step 10: Add the original line to the list
            # This preserves spaces and newline characters (\n)
            string_list.append(line)

    # Step 11: Return the list of customer data strings
    return string_list


# Read the file using the default filename
data = read_string_list()

# Display the first three customer entries
print(data[:3])