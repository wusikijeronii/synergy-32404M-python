def get_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

N = int(input())
arr = [*(get_factorial(i) for i in range(get_factorial(N), 0, -1))]
print(arr)
