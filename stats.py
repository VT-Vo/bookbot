def get_word_count(text):
    return f"Found {len(text.split())} total words"

def get_character_count(text):
    char_dict = dict()
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dictionary):
    return dictionary["num"]

def sort_dict_to_list(dictionary):
    char_num_list = list()
    for key in dictionary:
        char_num_list.append({"char": key, "num": dictionary[key]})
    char_num_list.sort(reverse=True, key=sort_on)
    return char_num_list
    
        
    