def print_recurse(container, start = 0):
    if start < len(container):
        print(container[start])
        print_recurse(container, start + 1)
    else:
        print("Конец списка")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print_recurse(my_list)
