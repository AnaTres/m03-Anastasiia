# Function to read input from file
def load_instructions(filepath):
    with open(filepath, 'r') as file:
        data = file.read().strip().split(',')
        return [cmd.strip() for cmd in data]  # Remove any extra whitespace


# Read movement instructions
file_name = 'day_2016_01.txt'  # Replace with actual file path
commands = load_instructions(file_name)
print(commands)


