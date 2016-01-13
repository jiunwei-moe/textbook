# Input
values = list(map(int, open("values.txt").read().splitlines()))
search = int(input("Enter search int: "))

# Process
index = int()
search_index = int()

index = 0
while index < len(values):
    if values[index] == search:
        search_index = index
        break
    index += 1
else:
    search_index = None

# Output
print(search_index)
