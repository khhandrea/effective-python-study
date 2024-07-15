from collections import defaultdict

class Cities:
    def __init__(self):
        self._data = defaultdict(set)

    def add(self, country, city):
        self._data[country].add(city)

    def __repr__(self):
        return "\n".join((str(item) for item in self._data.items()))

cities = Cities()
cities.add("Korea", "Seoul")
cities.add("Korea", "Busan")
cities.add("Italy", "Rome")

print(cities)