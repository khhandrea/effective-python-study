scores = (85, 83, 75, 93, 88, 92, 95, 72)

*others, second, first = sorted(scores)
worst, *others, first = sorted(scores)

print(f"first: {first}")
print(f"second: {second}")
print(f"worst: {worst}")