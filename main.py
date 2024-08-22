def main():
    # Relative path to the book we want to read. Assumes you are in the root of the repository
    book_path = "books/frankenstein.txt"
    
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)

    print(word_count)

# Read the contents of the file passed in by the argument `path`
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

# Count the number of words in a string pass in by the argument `text`
def count_words(text):
    # Split the string into a list of words. 
    # text.split() will split on all whitespace
    words = text.split()
    word_count = len(words)

    return word_count

main()
