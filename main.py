def main():
    # path to the book we want to read, configure user input later. Assumes you are in the root of the repository
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

# Read the contents of the file passed in by the argument `path`
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()
