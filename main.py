from stats import *
import sys


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    wc = word_count(text)
    print(f"Found {wc} total words")
    dict_list = sort_dict(letter_count(text))
    for d in dict_list:
        print(f"{d["letter"]}: {d["value"]}")


main()
