A = int(input())
B = int(input())

n = A
while n <= B:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()
