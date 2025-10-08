import sys
from stats import word_counter, character_counter, sort_char_counts

print(sys.argv)

file_path = "books/frankenstein.txt"

def get_book_text(file_path): 
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def main(): 

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    file_path = sys.argv[1]

    text = get_book_text(file_path) 
    num_words = word_counter(text)
    char_counts = character_counter(text)

   
    sorted_chars = sort_char_counts(char_counts)

   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
