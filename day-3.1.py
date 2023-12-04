import numpy as np

# Read input file
input_file = open("inputs/day-3.txt", "r")
input_file = input_file.read().splitlines()

input_matrix = []
for line in input_file:
    input_matrix.append(list(line))

input_matrix = np.array(input_matrix)

def symbol_bool(matrix: list) -> list:
    output = np.full(np.shape(matrix), False)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "." and not matrix[i][j].isdigit():
                for x in range(9):
                    a = (x // 3) - 1
                    b = (x % 3) - 1
                    try:
                        output[i+a][j+b] = True
                    except:
                        pass
    return output

def digit_bool(matrix: list) -> list:
    output = np.full(np.shape(matrix), False)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                output[i][j] = True
    return output

def extract_numbers(char_matrix, truth_matrix):
    output = np.full(np.shape(char_matrix), "")
    for i in range(len(truth_matrix)):
        for j in range(len(truth_matrix[i])):
            if truth_matrix[i][j]:
                output[i][j] = char_matrix[i][j]
            else:
                output[i][j] = " "
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

def sum_numbers(number_matrix) -> int:
    total = 0
    for row in number_matrix:
        numbers = "".join(row).split()
        for number in numbers:
            total += int(number)
    return total

symbols = symbol_bool(input_matrix)
digits = digit_bool(input_matrix)
is_number = np.logical_and(symbols, digits)
number_matrix = extract_numbers(input_matrix, is_number)
total = sum_numbers(number_matrix)

print(total)