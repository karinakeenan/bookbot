import sys 

from stats import get_num_words

from stats import num_of_char

from stats import sorted_list

def get_book_text(path):
        with open(path) as f:
                return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    char_counts = num_of_char(text)
    sorted_chars = sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


