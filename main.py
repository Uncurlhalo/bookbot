def main():
    # Relative path to the book we want to read. Assumes you are in the root of the repository
    book_path = "books/frankenstein.txt"
    
    # Get the text of the book
    book_text = get_book_text(book_path)
    # Get the count of words in the text, and a list of those words
    word_count, book_words = count_words(book_text)


# Read the contents of the file passed in by the argument `path`
# Return a string containing contents of the text file
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

# Count the number of words in a string pass in by the argument `text`
# Return the total number of words, and a list of the words
def count_words(text):
    # Split the string into a list of words. 
    # text.split() will split on all whitespace
    words = text.split()
    word_count = len(words)

    return word_count, words

main()
