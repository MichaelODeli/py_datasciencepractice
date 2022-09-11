en_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lowercase = 'abcdefghijklmnopqrstuvwxyz'
en_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
low_letters = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
digits = '0123456789'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!#$%&()*+,-./:;<=>?@[\\]^_`{|}~ '
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
all_options = ['letters', 
    'letters_bylang',  
    'symbols', 
    'digits',
    'symbol_count', 
    'uppercase', 
    'lowercase', 
    'uppercase_bylang', 
    'lowercase_bylang', 
    'all', 
    'spaces', 
    'all_nospaces'
]


def count_letters(string):
    k = 0
    for element in string:
        if element in letters: k+=1
    return k
def count_letters_bylang(string, lang):
    if lang == 'en':
        k = 0
        for element in string:
            if element in en_letters: k+=1
        return k
    elif lang == 'ru':
        k = 0
        for element in string:
            if element in ru_letters: k+=1
        return k
    elif lang == 'any':
        return(count_letters(string))
    else:
        raise ValueError("Invalid language '{}'. Supported only 'ru' and 'en'.".format(lang))
def count_symbols(string):
    k = 0
    for element in string:
        if element in symbols: k+=1
    return k
def count_digits(string):
    k = 0
    for element in string:
        if element in digits: k+=1
    return k
def count_symbol_count(string, symbols_to_count):
    k = 0
    if symbols_to_count != None:
        if symbols_to_count in symbols:
            for element in string:
                if element in symbols_to_count: k+=1
            return k
        else:
            raise ValueError("Invalid symbol '{}'.".format(symbols_to_count))
    else:
        raise ValueError("Please, specify symbol to count.")
def count_uppercase(string):
    k = 0
    for element in string:
        if element in up_letters: k+=1
    return k
def count_lowercase(string):
    k = 0
    for element in string:
        if element in low_letters: k+=1
    return k
def count_uppercase_bylang(string, lang):
    if lang == 'en':
        k = 0
        for element in string:
            if element in en_uppercase: k+=1
        return k
    elif lang == 'ru':
        k = 0
        for element in string:
            if element in ru_uppercase: k+=1
        return k
    elif lang == 'any':
        return(count_uppercase(string))
    else:
        raise ValueError("Invalid language '{}'. Supported only 'ru' and 'en'.".format(lang))
def count_lowercase_bylang(string, lang):
    if lang == 'en':
        k = 0
        for element in string:
            if element in en_lowercase: k+=1
        return k
    elif lang == 'ru':
        k = 0
        for element in string:
            if element in ru_lowercase: k+=1
        return k
    elif lang == 'any':
        return(count_lowercase(string))
    else:
        raise ValueError("Invalid language '{}'. Supported only 'ru' and 'en'.".format(lang))
def count_all(string):
    k = 0
    for element in string:
        if element in printable: k+=1
    return k
def count_spaces(string):
    k = 0
    for element in string:
        if element == ' ': k+=1
    return k
def count_all_nospaces(string):
    k = 0
    for element in string:
        if element in printable and element != ' ': k+=1
    return k

def symbolsCount(string, lang='any', options=['letters', 'symbols', 'all'], symbols_to_count=None):
    output = []
    for option in options:
        if option == 'letters':
            defResult = count_letters(string)
        elif option == 'letters_bylang':
            defResult = count_letters_bylang(string, lang)
        elif option == 'symbols':
            defResult = count_symbols(string)
        elif option == 'digits':
            defResult = count_digits(string)
        elif option == 'symbol_count':
            defResult = count_symbol_count(string, symbols_to_count)
        elif option == 'uppercase':
            defResult = count_uppercase(string)
        elif option == 'lowercase':
            defResult = count_lowercase(string)
        elif option == 'uppercase_bylang':
            defResult = count_uppercase_bylang(string, lang)
        elif option == 'lowercase_bylang':
            defResult = count_lowercase_bylang(string, lang)
        elif option == 'all':
            defResult = count_all(string)
        elif option == 'spaces':
            defResult = count_spaces(string)
        elif option == 'all_nospaces':
            defResult = count_all_nospaces(string)
        else: defResult = None
        output.append([option, defResult])
    return output
