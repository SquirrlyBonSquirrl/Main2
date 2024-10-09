"""
Module Docstring: main.py
======================

This is the main module of the read/write to file project.
"""

__author__ = "Nathan Adams"
__version__ = "0.1"
__license__ = "None"
__date__ = "October 7, 2024"

def read_file(file_name) -> None:
    """
    Reads a file and prints it to the console.
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def new_file(file_name) -> None:
    """
    Adds a new text file and writes data to it OR overwrites an existing file.
    """
    with open(file_name, "a") as f:
        f.write("Maine Coon")

def append_file(file_name, data) -> None:
    """
    Appends data to the existing file.
    """
    with open(file_name, "a") as f:
        f.write("\n")
        f.write(data)

def main():
    """
    Main entry point of the application.
    """
    user_input = input("Please enter your submission: ")
    append_file("cats.txt", user_input)

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()
