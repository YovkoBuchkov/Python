
# Write a Python program that takes a string representing a mathematical expression using Roman numerals (e.g., "X + V") and outputs the result in Roman numerals.
# Note: The Roman numeral system uses the following symbols:
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# Assume that the expression consists of two Roman numerals and an operator (+, -, *, or /), separated by spaces.
# Output the result in Roman numerals.
# Example:
# Input: X + V
# Output: XV

# new Roman numerals
# V̅ = 5,000
# X̅ = 10,000
# L̅ e за 50,000
# C̅ е за 100,000
# M̅ = 1,000,000


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num

def int_calc(s):
    first = s[0]
    second = s[2]
    operator = s[1]

    num1 = roman_to_int(first)
    num2 = roman_to_int(second)

    answer = 0
    if operator == '+':
        answer = num1 + num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '/':
        answer = num1 // num2

    return int_to_roman(answer)

def roman_to_int(s):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            total += roman_values[s[i]]
            i += 1

    return total


number = input().split(" ")
print(int_calc(number))