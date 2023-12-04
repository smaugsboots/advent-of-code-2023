import math

# Read input file
input_file = open("inputs/day-4.txt", "r")
input_file = input_file.read().splitlines()

def scratch_points(pile: list) -> list:
    "Calculate the number of points in a pile of scratchcards."

    total_points = 0

    # Iterate over each card in the pile
    for card in pile:
        # Extract the winning and selected numbers for each card
        scratchcard = card.split(": ")[1]
        nums = scratchcard.split(" | ")
        win_nums = set(nums[0].split())
        my_nums = set(nums[1].split())
        # Calculate the number of matches
        matches = set.intersection(win_nums, my_nums)
        num_matches = len(matches)
        # Calculate the number of corresponding points
        points = math.floor(2 ** (num_matches -  1))
        total_points += points
    
    return total_points
       
print(scratch_points(input_file))