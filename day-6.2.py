input_file = open("inputs/day-6.txt", "r")
input_file = input_file.read().splitlines()

def extract_records(records: list) -> list:
    """Extracts integer lists of the times and distances."""

    raw_time = records[0].split(": ")[1]
    time = int("".join(raw_time.split()))

    raw_distance = records[1].split(": ")[1]
    distance = int("".join(raw_distance.split()))

    return time, distance


def ways_to_win(time: int, distance: int) -> int:
    """Calculates the number of ways to win a race."""

    for t in range(time + 1):
        potential = t * (time - t)
        if potential > distance:
            return time - 2*t + 1

def margin_of_error(records: list) -> int:
    """Calculates the margin of error to win."""

    time, distance = extract_records(records)
    total = ways_to_win(time, distance)    
    print(total)

margin_of_error(input_file)