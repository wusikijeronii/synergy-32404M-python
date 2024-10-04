INPUT_STR = input()
isSame = INPUT_STR[::-1] == INPUT_STR
if isSame:
    print("yes")
else:
    print("no")
