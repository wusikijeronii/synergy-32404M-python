import random


def create_matrix():
    return [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]

def add_matrices(a, b):
    result = []
    for row1, row2 in zip(a, b):
        result_row = []
        for val1, val2 in zip(row1, row2):
            result_row.append(val1 + val2)
        result.append(result_row)
    return result

matrix1 = create_matrix()
print("Matrix 1:")
print(matrix1)

matrix2 = create_matrix()
print("\nMatrix 2:")
print(matrix2, '\n')

result_matrix = add_matrices(matrix1, matrix2)

for row in result_matrix:
    print(row)
