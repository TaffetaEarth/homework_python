def create_region(names, cities):
    created_region = {}
    for name, city in zip(names, cities):
        created_region[name] = city
    return created_region


def create_city(population, size):
    created_city = {"population": population, "size": size}
    return created_city


sochi = create_city(1000, 300)
krasnodar = create_city(400000, 1000)
print(create_region(["Sochi", "Krasnodar"], [sochi, krasnodar]))
