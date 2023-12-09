import numpy as np

input_file = open("inputs/day-9.txt", "r")
input_file = input_file.read().splitlines()

def generate_sequences(input: list) ->list:
    """Returns a list of lists, each of which is an integer sequence."""

    output = []
    for line in input:
        output.append(list(map(int, line.split())))
    return output

def extrapolate(sequence: list)-> int:
    """Returns the next term in the sequence."""

    differences = [sequence]

    # Find the set of differences between terms
    count = 0
    while True:
        seq = differences[count]
        jumps = []
        num_jumps = len(seq) - 1
        for i in range(num_jumps):
            jump = seq[i+1] - seq[i]
            jumps.append(jump)
        differences.append(jumps)
        count += 1
        if np.count_nonzero(jumps) == 0:
            break
    
    # Find the next term in each sequence of differences
    differences.reverse()
    num_differences = len(differences) - 1
    for i in range(num_differences):
        jump = differences[i][-1]
        next_term = differences[i+1][-1] + jump
        differences[i+1].append(next_term)
    
    return differences[-1][-1]

def extrapolate_sum(input: list) -> int:
    """Returns the sum of the next terms of a set of sequences."""

    sequences = generate_sequences(input)
    total = 0
    for item in sequences:
        total += extrapolate(item)
    print(total)

extrapolate_sum(input_file)