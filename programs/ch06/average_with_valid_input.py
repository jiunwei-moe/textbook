values = [3, 7, 9]

sum_values = float()
index = int()
average = float()

if len(values) > 0:
    sum_values = 0
    index = 0
    while index < len(values):
        sum_values += values[index]
        index += 1
    average = sum_values / len(values)
else:
    average = None

print(average)
