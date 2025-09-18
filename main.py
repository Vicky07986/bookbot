import sys 
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1] 

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

from stats import get_num_words, times_character_appears, sort_char_counts

def main():
    text = get_book_text(book_path)
    count = get_num_words(text)
    characters = times_character_appears(text)
    path = book_path
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------""")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted_counts = sort_char_counts(characters)
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
