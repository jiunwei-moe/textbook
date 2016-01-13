titles = list()
availability = list()
search = str()
index = int()

titles = open("titles.txt").read().splitlines()
availability = open("availability.txt").read().splitlines()
search = input("Enter title of book to check: ")
index = 0
while index < len(titles):
    if titles[index] == search:
        output = availability[index]
    index = index + 1
print(output)
