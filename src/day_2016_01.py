# Function to read input from file
def load_instructions(filepath):
    with open(filepath, 'r') as file:
        data = file.read().strip().split(',')
        return [cmd.strip() for cmd in data]  # Remove any extra whitespace


# Read movement instructions
file_name = 'day_2016_01.txt'  # Replace with actual file path
commands = load_instructions(file_name)
print(commands)


 #Function to calculate final distance
def compute_distance(commands, initial_heading="N"):
    position = {"N": 0, "E": 0, "S": 0, "W": 0}  # Track movement in all four directions
    headings = ["N", "E", "S", "W"]  # Define rotational order
    facing = initial_heading  # Current direction

    for cmd in commands:
        turn, steps = cmd[0], int(cmd[1:])  # Extract turn direction and step count

        if turn == "L":
            facing = headings[(headings.index(facing) - 1) % 4]  # Rotate left
        elif turn == "R":
            facing = headings[(headings.index(facing) + 1) % 4]  # Rotate right

        position[facing] += steps  # Move in the new direction

    # Compute net displacement
    vertical_displacement = abs(position["N"] - position["S"])
    horizontal_displacement = abs(position["E"] - position["W"])

    return vertical_displacement + horizontal_displacement


# Calculate total distance
total_distance = compute_distance(commands)
print("Total distance from start:", total_distance)


