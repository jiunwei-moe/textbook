values = list()
raw_input = str()
sum_values = float()
index = int()
average = float()

values = []
while True:
    raw_input = input("Enter integer, blank to end: ")
    if raw_input == "":
        break
    values += [int(raw_input)]

if len(values) > 0:
    sum_values = 0
    index = 0
    while index < len(values):
        sum_values += values[index]
        index += 1
    average = sum_values * len(values)
else:
    average = None

print(average)
