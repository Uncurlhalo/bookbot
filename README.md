# bookbot
Bookbot analyzes a provided text file and provides a report listing the following information

* The number of total words in the file
* The number of total characters in the file
* The count of how many times each character appears in the file, excluding non-alphabetic characters

## Installation and Use

* Clone the repository
* (Optional) Download or create text files to be analyzed, add their paths to the `config.txt` file
* Python must be installed on the system (this is out of scope of these instructions)
* Execute the command `./main.py` without arguments for interactive mode. 
* Read the help message for details on other CLI arguments.

### Configuration
An example config file, provided as `config.txt`, as well as the text of two public domain books have been provided in the `books` directory. The configuration file expects relative or absolute paths to plaintext files separated by spaces or new lines.

## Dependencies

* python version 3.10 or greater
* imports os, tkinter, and argparse. Installation of tkinter may be necessary on some systems.

## Acknowledgement
This project is based on the guided project course "Build a Bookbot" from [Boot.dev](https://www.boot.dev/tracks/backend)
