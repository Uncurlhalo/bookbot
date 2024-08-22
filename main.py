def main():
    # Relative path to the book we want to read. Assumes you are in the root of the repository
    book_path = "books/frankenstein.txt"
    
    # Get the text of the book
    book_text = get_book_text(book_path)
    # Get the count of words in the text, and a list of those words
    word_count, book_words = count_words(book_text)
    # Count the number of each character in the list of words
    book_chars_count = count_chars(book_words)


    print(book_chars_count)

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

# Count the number of each character in the list of words. Does not differentiate between capitals and lowercase
# Return a dict of all chars encountered and their counts
def count_chars(words):
    char_dict = {}
    for word in words:
        # loop over all chars in the word after lowering their case
        for char in word.lower():
            # if the char is not already in the dict, initialize its count as 1
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

main()
