import sys
from stats import get_book_text, character_frequency, put_sorted_dictionary

def check_usage():
    if (len(sys.argv) !=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return True

def count_all_the_words(in_this_string):
    
    split_words = in_this_string.split()
    return len(split_words)


def main():
    
    check_usage()
    book_to_get = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_get}...")

    print("----------- Word Count ----------")
    word_count = count_all_the_words(get_book_text(book_to_get))
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    input_character_string = get_book_text(book_to_get) 
    sorted_dic = put_sorted_dictionary(character_frequency(input_character_string))

    for item in sorted_dic:
        if (item["char"].isalpha()):
            print(f"{item["""char"""]}: {item["""num"""]}")
#    print(f"{put_sorted_dictionary(character_frequency(input_character_string))}")
    print("============= END ===============")
    exit(0)

if __name__ == "__main__":
    main()
