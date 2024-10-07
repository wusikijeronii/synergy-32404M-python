main_dict = {}

def get_pet(ID):
    return main_dict[ID] if ID in main_dict else {}

def pets_list():
    print(main_dict)

def make_pet():
    pets = {}
    key_tmp = input()
    value_tmp = {}
    value_tmp["Вид питомца"] = input()
    value_tmp["Возраст питомца"] = int(input())
    value_tmp["Имя владельца"] = input()
    pets[key_tmp] = value_tmp
    return pets


def create():
    main_dict[len(main_dict) + 1] = make_pet()


def get_suffix(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def read(read_id):
    pet = get_pet(read_id)
    if len(pet.items()) == 0:
        print("Такого питомца нет")
    for name, info in pet.items():
        age = info["Возраст питомца"]
        pet_type = info['Вид питомца']
        owner_name = info['Имя владельца']

        print(f"Это {pet_type} по кличке {name}. Возраст питомца: {age} "
              f"{get_suffix(age)}. Имя владельца: {owner_name}.")


def update(update_id):
    main_dict[update_id] = make_pet()

def delete(delete_id):
    del main_dict[delete_id]


command = ""
while command != "stop":
    command = input()
    if command == "create":
        create()
    elif command == "read":
        read(int(input()))
    elif command == "update":
        update(int(input()))
    elif command == "delete":
        delete(int(input()))
    elif command == "pets_list":
        pets_list()
