# Sort word in alphabitical order

# option->1
s = "Hello World".lower()
new_s = ""

word_list = s.split(" ")

for word in word_list:
    new_s += "".join(sorted(word)) + " "

new_s.rstrip()
print(new_s)
