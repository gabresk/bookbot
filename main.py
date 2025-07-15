import sys

from stats import word_count
from stats import count_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_chars(sorted_list, path, wc):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1] 
        text = get_book_text(path)
        wc = word_count(text)
        chars = count_char(text)

        print_chars(sort_dict(chars), path, wc)


main()

