# Input
values = list(map(int, open("values.txt").read().splitlines()))

# Process
maximum_value = float()
maximum_index = int()
index = int()

if len(values) > 0:
    maximum_value = values[0]
    maximum_index = 0
    index = 0
    while index < len(values):
        if values[index] > maximum_value:
            maximum_value = values[index]
            maximum_index = index
        index += 1
else:
    maximum_value = None
    maximum_index = None

# Output
print(maximum_value)
print(maximum_index)
