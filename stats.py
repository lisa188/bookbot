def word_count(text):
    '''
    Given some text, count the number words
    word_count: Str -> Int
    Examples:
        word_count("The Project Gutenberg eBook of Frankenstein") => 6
        word_count("") => 0
        word_count("Test") => 1
        word_count("There's two") => 2
    '''
    try:
        words_list = text.split()
        num_words = len(words_list)
        return num_words
    except Exception as e:
        print(f"Error encountered: {e}")


def character_count(text):
    '''
    Given some text, count the number of characters
    character_count: Str -> (dictof Str(1) Int)
    Examples:
        character_count("") => 0
        character_count("a") => 1
        character_count("this is a test") => 11
    '''
    lowercase_text = text.lower()
    char_counts = {}

    try:
        for character in lowercase_text:
            if character in char_counts:
                char_counts[character] += 1
            else:
                char_counts[character] = 1
        return char_counts
    except Exception as e:
        print(f"Error encountered: {e}")


def sort_dictionary(char_dict):
    '''
    Given a dictionary of characters
    return a sorted list of dictionaries from greatest to least
    sort_dictionary: (dictof Str Int) -> sorted (listof (dictof Str Str Str Int))
    Examples:
        sort_dictionary({}) => {}
        sort_dictionary({'a': 1}) => {'a': 1}
        sort_dictionary({'a': 1, 'b': 200}) => {'b': 200, 'a': 1}
    '''
    char_list = dict_to_dict_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def dict_to_dict_list(dict_of_chars):
    list_of_dicts = []
    for character in dict_of_chars:
        list_of_dicts.append({'character': character, 'count': dict_of_chars[character]})
    return list_of_dicts

def sort_on(dict):
    return dict["count"]