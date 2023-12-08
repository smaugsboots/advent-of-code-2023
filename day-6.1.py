input_file = open("inputs/day-6.txt", "r")
input_file = input_file.read().splitlines()

def extract_records(records: list) -> list:
    """Extracts integer lists of the times and distances."""

    raw_time = records[0].split(": ")[1]
    times = list(map(int, raw_time.split()))

    raw_distance = records[1].split(": ")[1]
    distances = list(map(int, raw_distance.split()))

    return times, distances


def ways_to_win(time: int, distance: int) -> int:
    """Calculates the number of ways to win a race."""

    for t in range(time + 1):
        potential = t * (time - t)
        if potential > distance:
            return time - 2*t + 1

def margin_of_error(records: list) -> int:
    """Calculates the margin of error to win."""

    times, distances = extract_records(records)

    total = 1
    for i in range(len(times)):
        total *= ways_to_win(times[i], distances[i])
    
    print(total)

margin_of_error(input_file)