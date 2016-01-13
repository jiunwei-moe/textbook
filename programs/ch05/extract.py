# Input
original = input("Enter original str: ")
test = str.isalnum

# Process
extract = str()
index = int()

extract = ""
index = 0
while index < len(original):
    if test(original[index]):
        extract += original[index]
    index += 1

# Output
print(extract)
