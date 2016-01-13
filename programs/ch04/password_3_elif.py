password = "P@55w0rd"
text = input("Enter text: ")
if text == "":
    print("Blank Input Not Allowed")
elif text == password:
    print("Yes Branch")
    print("Correct Password")
else:
    print("No Branch")
    print("Wrong Password")
print("Goodbye")
