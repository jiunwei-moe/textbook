titles = list()
availability = list()
search = str()
output = str()
index = int()

titles = open("titles.txt").read().splitlines()
availability = open("availability.txt").read().splitlines()
search = input("Enter title of book to check: ")
output = "Not Available"
index = 0
while index < len(titles):
    if titles[index] == search:
        output = availability[index]
    index = index + 1
print(output)
