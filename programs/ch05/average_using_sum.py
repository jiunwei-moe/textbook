# Input
values = list(map(int, open("values.txt").read().splitlines()))

# Process
sum_values = float()
average = float()

if len(values) > 0:
    sum_values = sum(values)
    average = sum_values / len(values)
else:
    average = None

# Output
print(average)
