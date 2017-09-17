cities = []
print("Reading city names from text file. Cities are:")
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))
for city in cities:
    print(city)