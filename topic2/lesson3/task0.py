animal_type_map = ["желторотый питон"]
animal_type_id = int(input())
animal_name = input()
animal_age = input()
if animal_type_id >= len(animal_type_map):
    raise IndexError("Invalid animal type ID")
print(f"{animal_type_map[animal_type_id]} по кличке \"{animal_name}\". Возраст: {animal_age}")
