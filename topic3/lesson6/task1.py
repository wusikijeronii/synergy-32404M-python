import math

X = int(input())
count = 0

for i in range(1, int(math.sqrt(X)) + 1):
    if X % i == 0:
        count += 1
        if i != X // i:
            count += 1
print(count)
