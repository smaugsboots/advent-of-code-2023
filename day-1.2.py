from operator import itemgetter

# Read input file
input_file = open("inputs/day-1.txt", "r")

# Convert input to a list, with each element corresponding to a line
input_file = input_file.readlines()

def calib_value(line: str) -> int:
    """Function to find calibration value of a line."""

    digits = []

    # Find numbers in digit form
    count = 0
    for char in line:
        if char.isdigit():
            digits.append([count, char])
        count += 1
    
    # Find numbers in string form
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers)):
        start = 0
        while True:
            index = line.find(numbers[i], start)
            if index >= 0:
                digits.append([index, str(i+1)])
                start = index + 1
            else:
                break
    
    # Sort numbers in by position in the line
    digits = sorted(digits, key=itemgetter(0))

    # Calculate calibration value
    value = digits[0][1] + digits[-1][1]
    return int(value)

# Find calibration value for each line
calibration_values = []
for line in input_file:
    calibration_values.append(calib_value(line))

# Sum calibration values
total = sum(calibration_values)
print(total)