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
            print(time - 2*t + 1)
            break

ways_to_win(*extract_records(input_file))