numbers = [int(i) for i in input().split()]
unique_numbers = set()
for i in numbers:
    if i in unique_numbers:
        print("YES")
    else:
        print("NO")
        unique_numbers.add(i)
