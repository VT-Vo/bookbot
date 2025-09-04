from stats import *
import sys

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    arguments = sys.argv
    if (not (len(arguments) == 2)):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(arguments[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arguments[1]}...")
    print("----------- Word Count ----------")
    print(get_word_count(text))
    print("--------- Character Count -------")

    char_list = sort_dict_to_list(get_character_count(text))
    for char_num_dict in char_list:
        if(char_num_dict["char"].isalpha()):
            print(f"{char_num_dict["char"]}: {char_num_dict["num"]}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()