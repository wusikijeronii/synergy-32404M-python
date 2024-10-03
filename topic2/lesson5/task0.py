# pylint: disable=invalid-name
number = int(input())

sign = ""
if number < 0:
    sign = "отрицательное"
elif number > 0:
    sign = "положительное"
else:
    sign = "нулевое"

EVEN = "" if number == 0 else " четное" if number % 2 == 0 else "нечетное"

print(f"{sign}{EVEN} число")
