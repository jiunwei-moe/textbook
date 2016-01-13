input_text = str()
acronym = str()
index = int()

input_text = input("Enter the input text:")
acronym = ""
index = 0
while index < len(input_text):
    if input_text[index-1].isspace():
        acronym += input_text[index]
    index += 1

print(acronym)
