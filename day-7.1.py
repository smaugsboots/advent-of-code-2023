import numpy as np
from operator import itemgetter

input_file = open("inputs/day-7.txt", "r")
input_file = input_file.read().splitlines()

def hand_and_bid(input: list) -> list:
    """Extracts seperate lists of the hands and their bids."""

    hands = []
    bids = []
    for line in input:
        split_line = line.split()
        hands.append(split_line[0])
        bids.append(int(split_line[1]))
    return hands, bids

def hand_type(hand: list) -> int:
    """Determines the type of a hand."""

    input_hand = [*hand]
    output_hand = [0] * 6
    card_freq = [0] * 13
    
    # Find frequency of each card and convert string value into numerical value
    for index, card in enumerate(input_hand):
        if card == "A":
            card_freq[12] += 1
            output_hand[index + 1] = 13
        elif card == "K":
            card_freq[11] += 1
            output_hand[index + 1] = 12
        elif card == "Q":
            card_freq[10] += 1
            output_hand[index + 1] = 11
        elif card == "J":
            card_freq[9] += 1
            output_hand[index + 1] = 10
        elif card == "T":
            card_freq[8] += 1
            output_hand[index + 1] = 9
        else:
            card_value = int(card)
            card_freq[card_value - 2] += 1
            output_hand[index + 1] = card_value - 1

    # Determine the type of the hand
    if max(card_freq) == 5:
        output_hand[0] = 7
    elif max(card_freq) == 4:
        output_hand[0] = 6
    elif max(card_freq) == 3 and np.count_nonzero(card_freq) == 2:
        output_hand[0] = 5
    elif max(card_freq) == 3:
        output_hand[0] = 4
    elif max(card_freq) == 2 and np.count_nonzero(card_freq) == 3:
        output_hand[0] = 3
    elif max(card_freq) == 2:
        output_hand[0] = 2
    else:
        output_hand[0] = 1
    
    return output_hand

def winnings(input: list):
    """Returns winnings from a set of hands and bids."""

    # Create a rankable list of hands
    hands, bids = hand_and_bid(input)
    rankable = []
    for index, hand in enumerate(hands):
        hand_and_type = hand_type(hand)
        hand_and_type.append(bids[index])
        rankable.append(hand_and_type)
    
    ranked_hands = sorted(rankable, key=itemgetter(0, 1, 2, 3, 4, 5))

    winnings = 0
    for rank, hand in enumerate(ranked_hands):
        winnings += (rank + 1) * hand[6]
    
    print(winnings)

winnings(input_file)