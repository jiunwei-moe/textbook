# Chapter 5 Review Question

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
        print(availability[index])
        break
    index = index + 1
else:
    print("Book not found")
