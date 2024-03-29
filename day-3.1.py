import numpy as np

# Read input file
input_file = open("inputs/day-3.txt", "r")
input_file = input_file.read().splitlines()

# Convert input into a matrix of characters
input_matrix = []
for line in input_file:
    input_matrix.append(list(line))
input_matrix = np.array(input_matrix)

def symbol_bool(char_matrix: np.array) -> np.array:
    """Returns a boolean matrix of which cells are adjacent to a symbol."""

    output = np.full(np.shape(char_matrix), False)
    for i in range(len(char_matrix)):
        for j in range(len(char_matrix[i])):
            if char_matrix[i][j] != "." and not char_matrix[i][j].isdigit():
                for x in range(9):
                    a = (x // 3) - 1
                    b = (x % 3) - 1
                    try:
                        output[i+a][j+b] = True
                    except:
                        pass
    return output

def digit_bool(char_matrix: np.array) -> np.array:
    """Returns a boolean matrix of which cells contain digits."""

    output = np.full(np.shape(char_matrix), False)
    for i in range(len(char_matrix)):
        for j in range(len(char_matrix[i])):
            if char_matrix[i][j].isdigit():
                output[i][j] = True
    return output

def extract_parts(char_matrix: np.array) -> np.array:
    """Returns a matrix of digits within part numbers, i.e. numbers which are adjacent to symbols."""

    symbols = symbol_bool(char_matrix)
    digits = digit_bool(char_matrix)
    truth_matrix = np.logical_and(symbols, digits)
    output = np.full(np.shape(char_matrix), "")

    # Find digits which are adjacent to symbols
    for i in range(len(truth_matrix)):
        for j in range(len(truth_matrix[i])):
            if truth_matrix[i][j]:
                output[i][j] = char_matrix[i][j]
            else:
                output[i][j] = " "

    # Find digits next to the digits adjacent to symbols, in order to find whole numbers
    for i in range(len(output)):
        for j in range(len(output[i])):
            if output[i][j].isdigit():
                count = 1
                while True and (j-count >= 0):
                    if char_matrix[i][j-count].isdigit():
                        output[i][j-count] = char_matrix[i][j-count]
                        count += 1
                    else:
                        break
                count = 1
                while True and (j+count < len(output[i])):
                    if char_matrix[i][j+count].isdigit():
                        output[i][j+count] = char_matrix[i][j+count]
                        count += 1
                    else:
                        break

    return output

def sum_numbers(number_matrix: np.array) -> int:
    """Returns the sum of numbers stored in digit form in a matrix."""

    total = 0
    for row in number_matrix:
        numbers = "".join(row).split()
        for number in numbers:
            total += int(number)
    return total

def sum_parts(char_matrix):
    """Returns the sum of part numbers."""

    parts = extract_parts(char_matrix)
    total = sum_numbers(parts)
    print(total)

sum_parts(input_matrix)