from stats import word_count
from stats import count_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    wc = word_count(text)
    chars = count_char(text)

    print(f"{wc} words found in the document")
    print(chars)
    print(sort_dict(chars))
main()

