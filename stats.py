def get_num_words(text):
    num_words = len(text.split())
    return num_words

def times_character_appears(text: str) -> dict:
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_count(entry):
        return entry["num"]

def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=get_count, reverse=True)
    return char_list
