#!/usr/bin/env python3
import os
import sys
import argparse
import tkinter as tk
from tkinter import filedialog

def main():
    try:
        # initialize a parser
        parser = argparse.ArgumentParser(
            prog='BookBot',
            description='A CLI tool for counting words and characters within text files'
        )
        # Make options mutually exclusive
        group = parser.add_mutually_exclusive_group()

        # Add parser arguments.
        # default to interactive mode
        # 1. Interactive mode: a boolean to determine if we want an interactive terminal session allowing for repeated entry of file paths
        group.add_argument('-i', '--interactive', action='store_true', help='Start an interactive session of BookBot', default=True)
        # 2. Path argument: a string representing a relative or absolute path to a file.
        group.add_argument('-p', '--path', action='store', help='A relative or absolute path to a text file you want analyzed by BookBot')
        # 3. Config argument: a string representing a relative or absolute path to a config file containing a list of file paths
        group.add_argument('-c', '--config', action='store', help='A relative or absolute file path to a text file containing a list of 1 or more file paths to text files you want analyzed by BookBot.')

        args = parser.parse_args()
        print(args)

        if args.path != None:
            analyze_text(args.path)
        elif args.config != None:
            process_config(args.config)
        elif args.interactive:
            interactive()
        else:
            print("How did we get here?")
    
    except KeyboardInterrupt:
        print("\nDetected Keyboard Interrupt, exiting...")
        quit()

# Define sorting parameter for our dict
def sort_on(dict):
    return dict["count"]

# Read the contents of the file passed in by the argument `path`
# Return a string containing contents of the text file
# Handle unicode exceptions and file not found exceptions
def get_file_text(path):
    try:
        with open(path, "rb") as f:
            try:
                file_contents = f.read().decode("utf-8")
                return file_contents, os.path.basename(path)
            except UnicodeDecodeError:
                print("Incompatible file type or file contents. Unicode characters are not supported.")
                return None, None
    except (FileNotFoundError, PermissionError) as e:
        print("File not found, path incorrect, or permission error on file")
        print(e)
        return None, None

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
    total_chars = 0
    for word in words:
        # loop over all chars in the word after lowering their case
        for char in word.lower():
            total_chars += 1
            # if the char is not already in the dict, initialize its count as 1
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict, total_chars

# Print out a report of all the information we've collected
def print_report(char_list_dict, word_count, char_count, text_name):
    # Print header of report with basic details
    print(f"--- Begin report of {text_name} ---")
    print(f"{word_count} words found in the document")
    print(f"{char_count} characters found in the document")

    for item in char_list_dict:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["count"]} times")
        else:
            continue
    print("--- End report ---")
    return

# Function to handle all the analysis function calls and print a report. Takes a path to a file, returns None
def analyze_text(path):
    content, text_name = get_file_text(path)
    word_count, text_words = count_words(content)
    chars_count_dict, char_count_total = count_chars(text_words)
    list_text_chars = [{"char": char, "count": count} for char, count in chars_count_dict.items()]
    list_text_chars.sort(reverse=True, key=sort_on)
    print_report(list_text_chars, word_count, char_count_total, text_name)

# Config read functions
def process_config(config):
    print("Attempting to read config")
    try:
        # open the config
        with open(config, "rb") as f:
            try:
                # get its contents
                config_contents = f.read().decode("utf-8")
                # split into a list of paths
                text_list_paths = config_contents.split()
            except UnicodeDecodeError:
                print("Incompatible file type or file contents. Unicode characters are not supported.")
                print("Exiting")
    except (FileNotFoundError, PermissionError) as e:
        print("File not found, path incorrect, or permission error on file")
        quit(e)
        
    # Tell the user we read their config, and list the paths to the files we'll analyze
    print("Config read successfully, found following list of texts:")
    print(text_list_paths)
    for path in text_list_paths:
        analyze_text(path)

# Interactive loop function
def interactive():
    # Continually loop until we get an exit command"
    while True:
        # Print a welcome message and provide some choices
        print("Welcome to BookBot! Please select an option:")
        print("1: Enter a file path")
        print("2: Browse for file")
        print("3: Exit the program")

        # take some input  from the user
        user_input = input("Make a selection (1/2/3): ").strip().lower()
        
        # use a switch case to choose our action
        match user_input:
            case "1":
                # get the path, analyze the book
                path = input("Enter an absolute or relative file path: ").strip()
                analyze_text(path)
            case "2":
                # open a file selection dialog
                root = tk.Tk()
                root.withdraw()
                path = filedialog.askopenfilename()
                # Check if they actually selected a file
                if path:
                    analyze_text(path)
                else:
                    print("No file was selected. Continuing...")
            case "3":
                print("Exiting")
                break
            case _:
                # default case, restart the loop
                print("- - - - - - - - - - - - - - - - -")
                print("Invalid option. Please try again")
                print("- - - - - - - - - - - - - - - - -")
    return

main()
