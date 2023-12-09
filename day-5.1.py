input_file = open("inputs/day-5.txt", "r")
input_file = input_file.read().split("\n\n")

def seed(input: list) -> list:
    """Returns a list of seed numbers."""

    seed_string = input[0].split(": ")[1]
    seed_list = list(map(int, seed_string.split()))
    return seed_list

def single_map(input: str) -> list:
    """Returns a map in list form from raw string form."""

    strings = input.split("\n")[1:]
    output = []
    for item in strings:
        output.append(list(map(int, item.split())))
    return output

def almanac_map(input: list) -> list:
    """Returns an almanac of maps."""

    output = []
    for item in input[1:]:
        output.append(single_map(item))
    return output

def map_path(seed: int, map: list) -> int:
    """Returns the destination of a seed through a given map."""

    for line in map:
        start = line[1]
        end = line[1] + line[2] - 1
        step = line[0] - line[1]
        if seed >= start and seed <= end:
            return seed + step
    return seed

def almanac_path(seed: int, maps: list) -> int:
    """Returns the destination of a seed through an almanac of maps."""

    location = seed
    for item in maps:
        location = map_path(location, item)
    return location

def closest_location(input: list) -> int:
    """Returns the closest location from a set of seeds and maps."""

    seeds = seed(input)
    maps = almanac_map(input)
    locations = []
    for item in seeds:
        locations.append(almanac_path(item, maps))
    print(min(locations))

closest_location(input_file)