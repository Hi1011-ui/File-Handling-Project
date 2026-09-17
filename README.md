# File and Folder Manager

A simple command-line File and Folder Manager built using Python.

This project allows the user to perform basic operations on files and folders directly from the terminal. It was created as a practice project while learning Python file handling and working with the `pathlib` and `shutil` modules.

## Features

The program provides different options for managing files and folders.

### Folder Operations

* Create a new folder
* View files and folders
* Rename a folder
* Delete a folder and its contents

### File Operations

* Create a new file
* Read file content
* Rename a file
* Append content to a file
* Overwrite existing file content
* Delete a file

### Input Handling

The program also handles some invalid inputs using `try-except` and checks whether the specified files or folders actually exist before performing operations.

## Menu Options

```text
1 : Create a folder.
2 : Read files and folders.
3 : Update the folder.
4 : Delete the folder.

5 : Create a file.
6 : Read files.
7 : Update the file.
8 : Delete the file.
0 : Exit the program.
```

## Technologies Used

* Python
* `pathlib`
* `shutil`
* File handling
* Functions
* `while` loop
* `if-elif-else`
* `try-except`
* User input

## Python Modules Used

### pathlib

The `pathlib` module is used to work with files and folders.

Some methods used in this project are:

```python
Path()
Path.mkdir()
Path.exists()
Path.is_dir()
Path.is_file()
Path.rename()
Path.unlink()
Path.rglob()
```

### shutil

The `shutil` module is used to delete folders along with their contents.

```python
shutil.rmtree()
```

## Example

```text
Options Guideline.

1 : Create a folder.
2 : Read files and folders.
3 : Update the folder.
4 : Delete the folder.

5 : Create a file.
6 : Read files.
7 : Update the file.
8 : Delete the file.
0 : Exit the program.

Choose Your Option: 5

Tell me new file name which you want to create with there extension: notes.txt
Write what you want in this file: Learning Python file handling

Your file is created successfully.
```

## What I Learned

I created this project to practice Python file handling and understand how Python can interact with files and folders on a computer.

While building this project, I practiced:

* Creating and managing folders using `pathlib`
* Creating and reading files
* Updating file contents
* Renaming files and folders
* Deleting files and folders
* Using `Path.exists()` to check whether something exists
* Using `Path.is_file()` and `Path.is_dir()`
* Finding files and folders using `rglob()`
* Using `shutil.rmtree()` to remove folders
* Creating reusable functions
* Using loops for menu-driven programs
* Handling invalid input with `try-except`

## About the Project

This is one of my Python practice projects. I built it while learning file handling, modules, functions, loops, and exception handling.

The main goal of this project was to understand how Python can be used to interact with the file system and perform common file and folder operations from the command line.
