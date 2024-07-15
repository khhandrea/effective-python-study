# bytes: 8bit sequence
# str: Unicode sequence

print("Hello, world")
print(b"Hello, world")
print()

print(repr("Hello, world"))
print(repr(b"Hello, world"))
print()

a = "Hello," + "world"
b = b"Hello," + b"world"
c = "Hello," + b"world" # Error