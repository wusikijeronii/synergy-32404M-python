def calculate_number(num):
    tens = (num // 10) % 10
    ones = num % 10
    hundreds = (num // 100) % 10
    thousands = (num // 1000) % 10
    ten_thousands = num // 10000

    calc_result = (tens ** ones) * hundreds
    divisor = ten_thousands - thousands
    if divisor != 0:
        calc_result /= divisor

    return calc_result

INPUT_NUMBER = 46275
output_result = calculate_number(INPUT_NUMBER)
print(output_result)
