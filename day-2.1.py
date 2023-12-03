# Read input file
input_file = open("inputs/day-2.txt", "r")
input_file = input_file.read().splitlines()

def decompose(game: str) -> list:
    """Converts each game from a line of text to a list of reveals.
    
    Each reveal is a list of the cubes revealed."""

    # Discard game ID to get the reveals
    game_extract = game.split(": ")
    game_extract = game_extract[1]

    # Split into a list of reveals
    split_game = game_extract.split("; ")

    # Split each reveal into a list of number of each colour cube revealed
    split_reveals = []
    for set in split_game:
        reveal = set.split(", ")
        split_reveals.append(reveal)
    
    return split_reveals

def possible(game: list, num_red: int, num_green: int, num_blue: int) -> bool:
    """Checks whether a game is possible based on number of each colour cube passed in."""

    # Check each reveal in a game
    possible_game = True
    for reveal in game:
        reds = 0
        greens = 0
        blues = 0

        # Extract numbr of red, greeen and blue cubes in each reveal
        for cubes in reveal:
            if cubes.find("red") >= 0:
                reds = int(cubes[:-3])
            elif cubes.find("green") >= 0:
                greens = int(cubes[:-5])
            elif cubes.find("blue") >= 0:
                blues = int(cubes[:-4])
        
        # Check if the reveal was possible
        possible_reveal = (reds <= num_red) and (greens <= num_green) and (blues <= num_blue)

        # If the reveal wasn't possible, the game wasn't possible
        if not possible_reveal:
            possible_game = False
            break

    return possible_game

# For each game, decompose it and check if the game was possible
count = 1       # Equal to game ID
sum_ID = 0      # Running total of valid game IDs
for line in input_file:
    game = decompose(line)
    if possible(game, 12, 13, 14):
        sum_ID += count
    count += 1

print(sum_ID)