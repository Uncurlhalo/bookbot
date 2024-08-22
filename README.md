# bookbot
Bookbot analyzes a provided text file and provides a report listing the following information

* The number of total words in the file
* The number of total characters in the file
* The count of how many times each character appears in the file, excluding non-alphabetic characters

## Installation and Use

* Clone the repository, or download the `main.py` file directly.
* edit the value of the variable `book_path` to contain a string with an absolute or relative path to a text file (Unicode characters are unsupported so please sanitize the input)
* Python must be installed on the system (this is out of scope of these instructions)
* Execute the command `python3 main.py`

## Dependencies

* python version >= 3.0

## Planned feature additions

* Support for files to be provided by a configuration file
* Support for interactive mode allowing the user to input a file path
* support for Unicode within text files
* Proper error handling for cases such as non-existent files, empty files, or unsupported file extensions

## Acknowledgement
This project is based on the guided project course "Build a Bookbot" from [Boot.dev](https://www.boot.dev/tracks/backend)
