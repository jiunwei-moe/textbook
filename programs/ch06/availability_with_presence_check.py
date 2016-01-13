import os
import sys

titles = list()
availability = list()
search = str()
output = str()
index = int()

if not os.path.isfile("titles.txt") or not os.path.isfile("titles.txt"):
    print("Data validation failed!")
    print("Both titles.txt and availability.txt should exist")
    sys.exit()
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
