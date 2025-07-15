from stats import word_count
from stats import count_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_chars(sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")

    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")



def main():
    text = get_book_text("books/frankenstein.txt")
    wc = word_count(text)
    chars = count_char(text)

    print_chars(sort_dict(chars))
main()

