from stats import get_num_words, get_book_text, get_num_characters, sort_char_counts
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book = get_book_text(book_path)

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")

    print("--------- Character Count -------")
    char_counts = get_num_characters(book)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        char = item['char']
        count = item['num']
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()