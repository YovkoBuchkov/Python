################################################################
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

# Пример за използване на функцията
decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(f"Двоичното представяне на {decimal_number} е {binary_number}")
################################################################
# 16 -> 2
def hex_to_binary(hex_number):
    # Първо, преобразуваме шестнадесетичното число в десетично
    decimal_number = int(hex_number, 16)

    # След това, преобразуваме десетичното число в двоично
    binary_number = bin(decimal_number)[2:]

    return binary_number


# Пример за използване на функцията
hex_number = "2A"
binary_number = hex_to_binary(hex_number)
print(f"Двоичното представяне на {hex_number} е {binary_number}")

################################################################
# 2 -> 16
def binary_to_hex(binary_number):
    # Първо, преобразуваме двоичното число в десетично
    decimal_number = int(binary_number, 2)

    # След това, преобразуваме десетичното число в шестнадесетично
    hex_number = hex(decimal_number)[2:].upper()

    return hex_number


# Пример за използване на функцията
binary_number = "101010"
hex_number = binary_to_hex(binary_number)
print(f"Шестнадесетичното представяне на {binary_number} е {hex_number}")


################################################################
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"

    is_negative = decimal_number < 0
    if is_negative:
        decimal_number = abs(decimal_number)

    binary_digits = []
    while decimal_number > 0:
        binary_digits.append(decimal_number % 2)
        decimal_number = decimal_number // 2

    binary_digits.reverse()  # Обърни списъка наопаки

    if is_negative:
        # Определяне на битовата дължина, тук взимаме 8 бита за примера
        bits = max(8, len(binary_digits) + 1)
        binary_digits = [0] * (bits - len(binary_digits)) + binary_digits

        # Допълващ код за представяне на отрицателни числа
        binary_digits = invert_bits(binary_digits)
        add_one_to_binary(binary_digits)
        if len(binary_digits) > bits:
            binary_digits = binary_digits[-bits:]
        binary_digits[0] = 1

    return ''.join(map(str, binary_digits))

################################################################
def invert_bits(binary_digits):
    return [1 - bit for bit in binary_digits]


def add_one_to_binary(binary_digits):
    carry = 1
    for i in range(len(binary_digits) - 1, -1, -1):
        if binary_digits[i] == 0:
            binary_digits[i] = 1
            carry = 0
            break
        else:
            binary_digits[i] = 0
    if carry == 1:
        binary_digits.insert(0, 1)


# Пример за използване на функцията
decimal_number = -42
binary_number = decimal_to_binary(decimal_number)
print(f"Двоичното представяне на {decimal_number} е {binary_number}")

################################################################