def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(text):
    return len(text.split())


def main():
    text = get_book_text("books/frankenstein.txt")
    wc = word_count(text)
    
    print(f"{wc} words found in the document")
main()

