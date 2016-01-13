# Quick Check 5.2

# Input
title = input("Enter title str: ")

# Process
result = True
for character in title:
    if not (character.isupper() or character.isspace()):
        result = False
        break

# Output
print(result)
