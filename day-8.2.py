import math

# Read input file
input_file = open("inputs/day-8.txt", "r")
input_file = input_file.read().splitlines()

def instructions(map: list) -> list:
    """Extracts the instructions from the map file and returns them as a list of indexes."""

    instruction_string = map[0]
    instructions = []
    for char in instruction_string:
        if char == "L":
            instructions.append(0)
        elif char == "R":
            instructions.append(1)
    return instructions

def nodes_elements(map: list) -> list:
    """Returns a list of node names and a list of pairs of elements."""

    raw_nodes = map[2:]
    nodes = []
    elements = []
    num_nodes = len(raw_nodes)
    for i in range(num_nodes):
        line = raw_nodes[i].split(" = ")
        node = line[0]
        element = line[1][1:-1].split(", ")
        nodes.append(node)
        elements.append(element)
    return nodes, elements

def start_nodes(nodes: list) -> list:
    """Returns a list of the indexes of starting nodes."""

    start_nodes = []
    for node in nodes:
        if node[-1] == "A":
            index = nodes.index(node)
            start_nodes.append(index)
    return start_nodes

def path(map: list) -> int:
    """Return the number of steps to navigate from starts to finishes."""

    i = instructions(map)
    n, e = nodes_elements(map)
    indexes = start_nodes(n)
    steps = []

    # Find the number of steps required to navigate to the end for each start node
    for x in range(len(indexes)):
        count = 0
        index = indexes[x]
        while True:
            instruction_index = count % len(i)
            next_instruct = i[instruction_index]
            next_node = e[index][next_instruct]
            count += 1
            if next_node[-1] == "Z":
                break
            else:
                index = n.index(next_node)
        steps.append(count)

    # Find the LCM of the steps required for each start node to find the overall steps required
    print(math.lcm(*steps))

path(input_file)