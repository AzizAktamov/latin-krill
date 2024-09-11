def latindan_crill(text):
    replacements = {
        "a": "а", "b": "б", "v": "в", "g": "г", "d": "д",
        "e": "е", "yo": "ё", "j": "ж", "z": "з", "i": "и",
        "y": "й", "k": "к", "l": "л", "m": "м", "n": "н",
        "o": "о", "p": "п", "r": "р", "s": "с", "t": "т",
        "u": "у", "f": "ф", "x": "х", "ts": "ц", "ch": "ч",
        "sh": "ш", "sch": "щ", "yu": "ю", "ya": "я",
        "A": "А", "B": "Б", "V": "В", "G": "Г", "D": "Д",
        "E": "Е", "Yo": "Ё", "J": "Ж", "Z": "З", "I": "И",
        "Y": "Й", "K": "К", "L": "Л", "M": "М", "N": "Н",
        "O": "О", "P": "П", "R": "Р", "S": "С", "T": "Т",
        "U": "У", "F": "Ф", "X": "Х", "Ts": "Ц", "Ch": "Ч",
        "Sh": "Ш", "Sch": "Щ", "Yu": "Ю", "Ya": "Я",
        # Add 'h' to 'ҳ' mapping if needed
        "h": "ҳ", "H": "Ҳ"
    }
    # To ensure 'h' is replaced correctly, process in a specific order if necessary
    for latin, crill in replacements.items():
        text = text.replace(latin, crill)
    return text

def latindan_arab(text):
    replacements = {
        "a": "ا", "b": "ب", "v": "ف", "g": "ج", "d": "د",
        "e": "ه", "j": "ج", "z": "ز", "i": "ي", "y": "ي",
        "k": "ك", "l": "ل", "m": "م", "n": "ن", "o": "و",
        "p": "ب", "r": "ر", "s": "س", "t": "ت", "u": "و",
        "f": "ف", "h": "ه", "x": "خ", "ch": "چ", "sh": "ش",
        "A": "ا", "B": "ب", "V": "ف", "G": "ج", "D": "د",
        "E": "ه", "J": "ج", "Z": "ز", "I": "ي", "Y": "ي",
        "K": "ك", "L": "ل", "M": "م", "N": "ن", "O": "و",
        "P": "ب", "R": "ر", "S": "س", "T": "ت", "U": "و",
        "F": "ف", "H": "ه", "X": "خ", "Ch": "چ", "Sh": "ش",
    }
    # Matnni Lotindan Arab alifbosiga o'zgartirish
    for latin, arab in replacements.items():
        text = text.replace(latin, arab)
    return text

def latindan_kores(text):
    replacements = {
        "a": "아", "b": "ㅂ", "v": "ㅍ", "g": "ㄱ", "d": "ㄷ",
        "e": "에", "j": "ㅈ", "z": "ㅈ", "i": "이", "y": "ㅣ",
        "k": "ㅋ", "l": "ㄹ", "m": "ㅁ", "n": "ㄴ", "o": "오",
        "p": "ㅍ", "r": "ㄹ", "s": "ㅅ", "t": "ㅌ", "u": "우",
        "f": "ㅍ", "x": "ㅅ", "ch": "ㅊ", "sh": "ㅅ",  # Replace 'sh' with 'ㅅ' for Korean
        "h": "ㅎ"  # Add mapping for 'h'
    }
    for latin, kores in replacements.items():
        text = text.replace(latin, kores)
    return text


# Kirilldan Lotinga o'zgartirish funksiyasi
def crilldan_latin(text):
    replacements = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
        "е": "e", "ё": "yo", "ж": "j", "з": "z", "и": "i",
        "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
        "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
        "у": "u", "ф": "f", "х": "x", "ц": "ts", "ч": "ch",
        "ш": "sh", "щ": "sch", "ю": "yu", "я": "ya",
        "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
        "Е": "E", "Ё": "Yo", "Ж": "J", "З": "Z", "И": "I",
        "Й": "Y", "К": "K", "Л": "L", "М": "M", "Н": "N",
        "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
        "У": "U", "Ф": "F", "Х": "X", "Ц": "Ts", "Ч": "Ch",
        "Ш": "Sh", "Щ": "Sch", "Ю": "Yu", "Я": "Ya",
        "ҳ": "h", "Ҳ": "H",
        "қ": "q", "Қ": "Q", "ғ": "g'", "Ғ": "G'", "ў": "o'", "Ў": "O'",
        "йў": "yo", "Йў": "Yo"
    }
    # Kirill harflarini Lotin harflariga almashtirish
    for crill, latin in replacements.items():
        text = text.replace(crill, latin)
    return text


def arabdan_latin(text):
    replacements = {
        "ا": "a", "ب": "b", "ت": "t", "ث": "th", "ج": "j",
        "ح": "h", "خ": "kh", "د": "d", "ذ": "dh", "ر": "r",
        "ز": "z", "س": "s", "ش": "sh", "ص": "s'", "ض": "d'",
        "ط": "t'", "ظ": "z'", "ع": "‘", "غ": "gh", "ف": "f",
        "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n",
        "ه": "h", "و": "w", "ي": "y", "ء": "'", "ئ": "'y",
        "ؤ": "'w", "ى": "a"
    }
    # Arab harflarini Lotin harflariga almashtirish
    for arab, latin in replacements.items():
        text = text.replace(arab, latin)
    return text


def koresdan_latin(text):
    replacements = {
        "ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt",
        "ㄹ": "r", "ㅁ": "m", "ㅂ": "b", "ㅃ": "pp", "ㅅ": "s",
        "ㅆ": "ss", "ㅇ": "-", "ㅈ": "j", "ㅉ": "jj", "ㅊ": "ch",
        "ㅋ": "k", "ㅌ": "t", "ㅍ": "p", "ㅎ": "h",
        "ㅏ": "a", "ㅐ": "ae", "ㅑ": "ya", "ㅒ": "yae", "ㅓ": "eo",
        "ㅔ": "e", "ㅕ": "yeo", "ㅖ": "ye", "ㅗ": "o", "ㅘ": "wa",
        "ㅙ": "wae", "ㅚ": "oe", "ㅛ": "yo", "ㅜ": "u", "ㅝ": "wo",
        "ㅞ": "we", "ㅟ": "wi", "ㅠ": "yu", "ㅡ": "eu", "ㅢ": "ui",
        "ㅣ": "i"
    }
    # Koreys harflarini Lotin harflariga almashtirish
    for kores, latin in replacements.items():
        text = text.replace(kores, latin)
    return text


