input_file = open("inputs/day-5.txt", "r")
input_file = input_file.read().split("\n\n")

def seed(input: list) -> list:
    """Returns a list defining seed ranges."""

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
    output.reverse()
    return output

def map_path(seed: int, map: list) -> int:
    """Returns the origin of a location through a given map."""

    for line in map:
        start = line[0]
        end = line[0] + line[2] - 1
        step = line[1] - line[0]
        if seed >= start and seed <= end:
            return seed + step
    return seed

def almanac_path(seed: int, maps: list) -> int:
    """Returns the origin of a location through an almanac of maps."""

    location = seed
    for item in maps:
        location = map_path(location, item)
    return location

def seed_source(origin: int, seed_list: list) -> bool:
    """Checks if an origin is within a given list of seed ranges."""

    for i in range(int(len(seed_list) / 2)):
        start = seed_list[2*i]
        end = seed_list[2*i] + seed_list[2*i + 1] - 1
        if origin >= start and origin <= end:
            return True
    return False

def closest_location(input: list) -> int:
    """Returns the closest location from a set of seeds and maps."""

    seeds = seed(input)
    maps = almanac_map(input)
    location = 0
    while True:
        origin = almanac_path(location, maps)
        if seed_source(origin, seeds):
            print(location)
            break
        else:
            location += 1

closest_location(input_file)    
# Solution took ~6 minutes to calculate