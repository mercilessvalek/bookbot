def word_count(filename):
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
        num_words = len(contents.split())
    return num_words, contents


def character_count(text):
    char_count = {}
    for char in text.lower():  # Convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include letters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda x: x["num"], reverse=True)  # Sort descending by count
    return sorted_list

