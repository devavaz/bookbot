def get_book_text(filepath): 
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(book): 
    lowered_text = book.lower()
    character_num = {}

    for character in lowered_text: 
        if character in character_num:
            character_num[character] += 1
        else:
            character_num[character] = 1

    return character_num      

def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
