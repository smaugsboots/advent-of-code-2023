import math

# Read input file
input_file = open("inputs/day-4.txt", "r")
input_file = input_file.read().splitlines()

def scratch_cards(pile: list) -> list:
    "Calculate the number of points in a pile of scratchcards."

    total_cards = [1] * len(pile)

    # Iterate over each card in the pile
    card_index = 0
    for card in pile:
        # Extract the winning and selected numbers for each card
        scratchcard = card.split(": ")[1]
        nums = scratchcard.split(" | ")
        win_nums = set(nums[0].split())
        my_nums = set(nums[1].split())
        # Calculate the number of matches
        matches = set.intersection(win_nums, my_nums)
        num_matches = len(matches)
        # Calculate the number of cards won
        for i in range(1, num_matches + 1):
            total_cards[card_index + i] += total_cards[card_index]
        card_index += 1
    
    return sum(total_cards)
       
print(scratch_cards(input_file))