alnum_to_morse_code = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
    '-':'-....-', '(':'-.--.', ')':'-.--.-'
}

def to_morse_code(message_to_decode):
    decoded_words = ""
    for code in message_to_decode:
        if code == ' ':
            decoded_words += '|' + ' '
        else:
            decoded_words += alnum_to_morse_code.get(code, '') + " "
    return decoded_words


line = input().upper()
decode = to_morse_code(line)

print(decode)

morse_to_alnum = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9", '--..--':', ', '.-.-.-':'.', '..--..':'?',
    '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')'
}

def morse_to_alfa(message_to_decode):
    decoded_words = ""
    for code in message_to_decode:
        if code == '|' or code == '/':
            decoded_words += ' '
        else:
            decoded_words += morse_to_alnum.get(code, '')

    return decoded_words


line = input().split(' ')

decode = morse_to_alfa(line)
print(decode)

