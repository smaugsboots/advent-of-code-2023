import numpy as np

# Read input file
input_file = open("inputs/day-3.txt", "r")
input_file = input_file.read().splitlines()

# Convert input into a matrix of characters
input_matrix = []
for line in input_file:
    input_matrix.append(list(line))
input_matrix = np.array(input_matrix)

def gear_bool(matrix: np.array) -> np.array:
    """Returns two matrices:
    1. A boolean matrix of which cells are adjacent to the first gear found
    2. A vesrion of the input matrix with the gear that was found removed, or False if no gear was found."""

    symbol_output = np.full(np.shape(matrix), False)
    char_output = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                char_output[i][j] = "."
                for x in range(9):
                    a = (x // 3) - 1
                    b = (x % 3) - 1
                    try:
                        symbol_output[i+a][j+b] = True
                    except:
                        pass
                return symbol_output, char_output
    return symbol_output, False

def digit_bool(matrix: np.array) -> np.array:
    """Returns a boolean matrix of which cells contain digits."""

    output = np.full(np.shape(matrix), False)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                output[i][j] = True
    return output

def extract_parts(char_matrix: np.array, truth_matrix: np.array) -> np.array:
    """Returns a matrix of digits within part numbers, i.e. numbers which are adjacent to symbols."""

    output = np.full(np.shape(char_matrix), "")

    # Find digits which are adjacent to symbols
    for i in range(len(truth_matrix)):
        for j in range(len(truth_matrix[i])):
            if truth_matrix[i][j] and char_matrix[i][j].isdigit():
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

def gear_ratio(number_matrix: np.array) -> int:
    """Returns the gear ratio of parts adjacent to a gear."""

    rows = []
    for row in number_matrix:
        numbers = "".join(row).split()
        for i in range(len(numbers)):
            rows.append(int(numbers[i]))
    if len(rows) == 2:
        return np.prod(rows)
    else:
        return 0

def sum_ratios(input_matrix: np.array) -> int:
    """Returns the sum of gear ratios."""

    sum = 0
    digits = digit_bool
    char_matrix = input_matrix
    while True:
        gear, char_matrix = gear_bool(char_matrix)
        filter = np.logical_and(gear, digits)
        numbers = extract_parts(input_matrix, filter)
        sum += gear_ratio(numbers)
        if char_matrix is False:
            break
    print(sum)

sum_ratios(input_matrix)