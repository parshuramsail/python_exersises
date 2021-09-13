# Check if a string starts with a Prefix

# option -> 1
s = "Hello"
prefix = "He"
print(s[:len(prefix)] == prefix)

# option -> 2
s = "Hello"
print(s.startswith("He"))
