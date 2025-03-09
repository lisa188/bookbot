import sys
from stats import word_count, character_count, sort_dictionary

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]

    text = get_book_text(bookpath)
    num_words = word_count(text)
    #print(f"{num_words} words found in the document")
    char_counts = character_count(text)
    sorted_list = sort_dictionary(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_char_counts(sorted_list)


def get_book_text(path_to_file):
    '''
    Given a filepath, return the contents of the file
    get_book_text: Str -> Str
    Examples:
        get_book_text("books/frankenstein.txt") => "The Project Gutenberg eBook of Frankenstein..."
        get_booK_text("books") => error
        get_book_text(123) => error
    '''
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print(f"Error encountered: {e}")


def print_char_counts(sorted_list):
    for dict in sorted_list:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    

main()