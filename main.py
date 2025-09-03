from stats import *

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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