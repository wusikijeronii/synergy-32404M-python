def get_year_suffix(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


pets = {}
key_tmp = input()
value_tmp = {}
value_tmp["Вид питомца"] = input()
value_tmp["Возраст питомца"] = int(input())
value_tmp["Имя владельца"] = input()
pets[key_tmp] = value_tmp

for name, info in pets.items():
    age = info["Возраст питомца"]
    pet_type = info['Вид питомца']
    owner_name = info['Имя владельца']

    print(f"Это {pet_type} по кличке {name}. Возраст питомца: {age} "
          f"{get_year_suffix(age)}. Имя владельца: {owner_name}.")
