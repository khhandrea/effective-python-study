grade_counts = {
    "A": 3,
    "B": 5,
    "C": 2
}

query = "B+"

# 1
count = grade_counts.get(query, 0)
grade_counts[query] = count + 1

# 2
if grade_counts.get(query) is None:
    grade_counts[query] = 1
else:
    grade_counts[query] += 1