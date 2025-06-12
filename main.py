import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import word_count, character_count, sort_character_counts

def main():
    count, text = word_count(sys.argv[1])
    print(f"Found {count} total words")  # ✅ Must match exactly

    char_freq = character_count(text)
    sorted_characters = sort_character_counts(char_freq)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")  # ✅ Must match expected format

main()

