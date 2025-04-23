import sys
from stats import count_words, count_letters, print_letter_counts


def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_letter_counts(count_letters(book_text.lower()))
    print("============= END ===============")


if __name__ == '__main__':
    main()
