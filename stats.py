# stats.py

def word_counter(text):
    return len(text.split())

def character_counter(text): 
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
            if char in char_counts:
                char_counts[char] += 1
            else: 
                char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    # Step 1: convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    # Step 2: sort the list by 'num' in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
