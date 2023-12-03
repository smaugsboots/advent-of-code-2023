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

def power(game: list) -> int:
    """Finds the minimum number of each colour cube required for a game to be possible, 
    and calculates the power of thi set of cubes."""

    min_reds = 0
    min_greens = 0
    min_blues = 0

    # Check each reveal in a game
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
        
        # Check if the reveal changes minimum number of cubes required
        if reds > min_reds:
            min_reds = reds
        if greens > min_greens:
            min_greens = greens
        if blues > min_blues:
            min_blues = blues

    # Calculate the power of the minimum set of cubes
    cubes_power = min_reds * min_blues * min_greens
    return cubes_power

# For each game, decompose it and find the power of the miminum set of cubes required
sum_power = 0
powers = []
for line in input_file:
    sum_power += power(decompose(line))

print(sum_power)