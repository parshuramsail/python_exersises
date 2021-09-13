# Print character at a given index

string = "Hello"
i = 0

if not string:
    print("Empty string")
elif i < len(string):
    print(string[i])
else:
    print("i out of range")
