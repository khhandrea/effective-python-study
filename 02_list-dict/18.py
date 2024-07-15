class Cities(dict):
    def __missing__(self, key):
        print(f"New city added: {key}")
        self[key] = set()
        return self[key]

    def add(self, country, city):
        self[country].add(city)

    def __repr__(self):
        return "\n".join((str(item) for item in self.items()))

cities = Cities()
cities.add("Korea", "Seoul")
cities.add("Korea", "Busan")
cities.add("Italy", "Rome")

print(cities)