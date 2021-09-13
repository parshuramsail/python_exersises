# Remove spaces from string

# option->1
s = "Hello, world"
new_s = ""

for char in s:
    if char != " ":
        new_s += char
print(new_s)


# option->2

s = "hello, world"
print(s.replace(" ", ""))
