This asks the user what cat to add to cats.txt file and adds it based on user input.

also try this

"""
Module Docstring: main.py
======================

This is the main module of the read/write to file project.
"""

__author__ = "Nathan Adams"
__version__ = "0.1"
__license__ = "None"
__date__ = "October 7, 2024"

def read_file(file_name="cats.txt") -> None:
    """
    Reads a file and prints it to the console.
    """
    try:
        with open(file_name, "r") as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

def new_file(file_name="cats.txt") -> None:
    """
    Creates a new text file and writes data to it OR overwrites an existing file.
    """
    with open(file_name, "w") as f:  # Use "w" to overwrite or create a new file
        f.write("Maine Coon\n")  # Add a newline after initial text

def append_file(file_name="cats.txt", data="") -> None:
    """
    Appends data to the existing file on a new line.
    """
    with open(file_name, "a") as f:
        f.write(f"{data}\n")  # Ensure data is written on a new line

def main(user_input=None):
    """
    Main entry point of the application.
    """
    if user_input is None:  # If no input is provided, ask the user
        user_input = input("Please enter your submission: ")
    append_file("cats.txt", user_input)

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()
