# Change commas by dot in string

# option->1
# s = 'Hello, world'
# new_s = ''

# comma = ','
# dot = '.'

# for char in s:
#     if char == comma:
#         new_s += dot
#     else:
#         new_s += char
# print(new_s)

# option->2

s = 'Hello, World'
print(s.replace(',', '.'))
