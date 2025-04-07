from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def main():
    contents = get_book_text(sys.argv[1])
    num_words = word_count(contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    count_dict = report(character_count(contents))
    for char, count in count_dict.items():
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")


main()

