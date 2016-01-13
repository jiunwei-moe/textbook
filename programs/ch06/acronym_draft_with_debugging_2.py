input_text = str()
acronym = str()
index = int()

input_text = input("Enter the input text: ")
acronym = ""
index = 0
while index < len(input_text):
    if input_text[index-1].isspace() or index == 0:
        acronym += input_text[index]
    print("Debug: when index = " + str(index) + ", acronym = " + acronym)
    index += 1

print(acronym)
