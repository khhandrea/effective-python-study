def get_first_positive(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

color = {
    "red": [5, 3],
    "green": [0],
    "blue": []
}

first_red = get_first_positive(color, 'red')
print(first_red)