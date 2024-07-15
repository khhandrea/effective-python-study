food = {
    'fruit': ('apple', 500),
    'snack': ('pancake', 2000),
    'vegetable': ('tomato', 3000)
}

food_db = {
    "fruit": ("apple", 500),
    "snack": ("pancake", 2000),
    "vegetable": ("tomato", 3000)
}

for category, (name, cost) in food_db.items():
    print(f"{name:10s} in {category:10s} | {cost:>4d} KRW")