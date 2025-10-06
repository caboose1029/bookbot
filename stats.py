def count_words(text: str) -> int:
    words = text.split()
    count = len(words)
    return count

def count_chars(text: str):
    chars = {}
    text = text.lower()
    for i in range(len(text)):
        char = text[i]
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def generate_report(chars):
    sorted = []
    for key, value in chars.items():
        char = {}
        char["char"] = key
        char["num"] = value
        sorted.append(char)


    sorted.sort(reverse=True, key=sort_on)
    return sorted




