# Read input file
input_file = open("inputs/day-1.txt", "r")

# Convert input to a list, with each element corresponding to a line
input_file = input_file.readlines()

# Define function to find calibration value in a line
def calib_value(line: str) -> int:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    value = digits[0] + digits[-1]
    return int(value)

# Find calibration value for each line
calibration_values = []
for line in input_file:
    calibration_values.append(calib_value(line))

# Sum calibration values
total = sum(calibration_values)
print(total)