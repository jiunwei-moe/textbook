input_text = str()
acronym = str()
index = int()

input_text = input("Enter the input text: ")
acronym = ""
index = 0
while index < len(input_text):
    if (input_text[index-1].isspace() or index == 0) and not input_text[index].isspace():
        acronym += input_text[index]
    index += 1
acronym = acronym.upper()

print(acronym)
