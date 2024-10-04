def change_array(arr):
    last = arr.pop()
    arr.insert(0, last)


N = int(input())
numbers = [int(i) for i in input().split()]
change_array(numbers)
print("Result:", *numbers)
