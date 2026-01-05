def sort_on(items):
    return items["num"]

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def character_frequency(input_character_string):
    character_dictionary = dict()
    for i in range(0, len(input_character_string)):
        if input_character_string[i].lower() in character_dictionary:
            character_dictionary[input_character_string[i].lower()] +=1
        else:
            character_dictionary[input_character_string[i].lower()] =1
    return character_dictionary

def put_sorted_dictionary(input_dictionary):
    sorted_dict_list = []
    for entry in input_dictionary:
        sorted_dict_list.append({"char": entry, "num": input_dictionary[entry]})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

