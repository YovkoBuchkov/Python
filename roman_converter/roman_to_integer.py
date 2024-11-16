
roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

s = input()

result = 0
sim = ""
pim = ""

for i, n in enumerate(s):
    pim = n
    result += roman_numerals[s[i]]

    if sim == "I" and (pim == "V" or pim == "X"):
        result -= 2
    elif sim == "X" and (pim == "L" or pim == "C"):
        result -= 20
    elif sim == "C" and (pim == "D" or pim == "M"):
        result -= 200

    sim = n

print(result)


# Input: s = "III"
# Output: 3
#
# Input: s = "LVIII"
# Output: 58
#
# Input: s = "MCMXCIV"
# Output: 1994


# V̅ = 5,000
# X̅ = 10,000
# M̅ = 1,000,000
#DCCCLXXXVIII = 500 + 100 + 100 + 100 + 50 + 10 + 10 + 10 5 + 1 + 1 + 1 = 888
# MCMXC = 1000 + 900 + 90 = 1990
# MCMXCI = 1000 + 900 + 90 + 1 = 1991
# MCMXCII = 1000 + 900 + 90 + 2 = 1992
# MCMXCIII = 1000 + 900 + 90 + 3 = 1993
# MCMXCIV = 1000 + 900 + 90 + 4 = 1994
# MCMXCV = 1000 + 900 + 90 + 5 = 1995
# MCMXCVI = 1000 + 900 + 90 + 6 = 1996
# MCMXCVII = 1000 + 900 + 90 + 7 = 1997
# MCMXCVIII = 1000 + 900 + 90 + 8 = 1998
# MCMXCIX = 1000 + 900 + 90 + 9 = 1999



# def roman_to_int(s):
#     """
#     Обяснение на алгоритъма:
#     Речник: Имаме речник roman_values, в който всяка римска цифра е свързана със съответната си числена стойност.
#     Обхождане: Обхождаме всяка цифра от низа.
#     Ако стойността на следващата цифра е по-голяма от текущата, изваждаме стойността на текущата цифра.
#     В противен случай прибавяме стойността на текущата цифра.
#     Резултат: Крайният резултат се връща като цяло число.
#     Args: Romans simbols
#         s:
#
#     Returns: integer
#
#     """
#     roman_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#
#     total = 0
#
#     for i in range(len(s)):
#         current_value = roman_values[s[i]]
#
#         if i + 1 < len(s) and roman_values[s[i + 1]] > current_value:
#             total -= current_value
#         else:
#             total += current_value
#
#     return total
#
# s = input("Въведете римска цифра: ")
# print(f"Резултат: {roman_to_int(s)}")
# print(help(roman_to_int))


################################################################

# roman_values = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
#
#
# for symbol, value in roman_values.items():
#     if value == 10:
#         print(f"Symbol: {symbol}")  # Изход: X


################################################################
# keys = roman_values.keys()
# print(keys)  # Изход: dict_keys(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
#
# #or
#
# keys_list = list(roman_values.keys())
# print(keys_list)  # Изход: ['I', 'V', 'X', 'L', 'C', 'D', 'M']
