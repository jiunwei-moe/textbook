# Input
values = list(map(int, open("values.txt").read().splitlines()))

# Process
minimum_value = float()
minimum_index = int()
index = int()

if len(values) > 0:
    minimum_value = values[0]
    minimum_index = 0
    index = 0
    while index < len(values):
        if values[index] < minimum_value:
            minimum_value = values[index]
            minimum_index = index
        index += 1
else:
    minimum_value = None
    minimum_index = None

# Output
print(minimum_value)
print(minimum_index)
