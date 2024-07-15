names = ("Freude", "Kevin", "Charlie")
lens = (len(name) for name in names)

longest_name = ""
for name, length in zip(names, lens):
    if length > len(longest_name):
        longest_name = name

print(f"The longest name is {longest_name}")