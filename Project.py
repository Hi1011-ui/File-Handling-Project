from pathlib import Path
import shutil

def create_folder():

    try:
        name = input("Enter a new folder name: ")
        p = Path(name)
        p.mkdir()
        print("Your folder is created successfully.")

    except Exception as err:
        print(f"Your error is {err}")

def read_folder():

    try:
        p = Path("")
        items = list(p.rglob('*'))
        for i, v in enumerate(items):
            print(f"{i+1}: {v}")

    except Exception as err:
        print(f"Your error is {err}")

def update_folder():

    try:
        read_folder()
        old_name = input("Tell me name of folder which you want to update: ")
        p = Path(old_name)

        if p.exists() and p.is_dir():
            new_name = input("Tell me new name of folder: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder is updated successfully.")

        else:
            print("No such folder is exist.")

    except Exception as err:
        print(f"Error occured as {err}")

def delete_folder():

    try:
        read_folder()
        name = input("Tell me name of folder which you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder is deleted successfully.")

        else:
            print("No such folder is exists.")

    except Exception as err:
        print(f"Error occured as {err}")

def create_file():
    try:
        read_folder()
        name = input("Tell me new file name which you want to create with there extension: ")
        p = Path(name)

        if not p.exists():
            with open(name, 'w') as fs:
                data = input("Write what you want in this file: ")
                fs.write(data)

            print("Your file is created successfully.")

        else:
            print("This file is already exists.")

    except Exception as err:
        print(f"An error occured as {err}")

def read_file():

    try:
        read_folder()
        name = input("Tell me which file you have to read with there extension: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(name, 'r') as fs:
                content = fs.read()
                print("Your file content is: \n")
                print(content)

        else:
            print("File does not exists.")
    except Exception as err:
        print(f"An error occured as {err}")

def update_file():

    try:
        read_folder()
        name = input("Tell me which file you want to update with there extension: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Options for which thing you have to update.\n")
            print("1: Rename a file.")
            print("2: Append something in file.")
            print("3: Overwrite the file.")

            choice = int(input("Select a option: "))

            if choice == 1:
                new_name = input("Tell me new name of this file with there extension: ")
                new_p = Path(new_name)

                if not new_p.exists():
                    p.rename(new_name)
                    print("File name is change successfully.")

                else:
                    print("File name already exists.")

            elif choice == 2:
                with open(name, 'a') as fs:
                    content = input("Write what you want to append: ")
                    fs.write(" " + content)
                    print("Your content is appended successfully.")

            elif choice == 3:
                with open(name, 'w') as fs:
                    content = input("Write what you want to append: ")
                    fs.write(" " + content)
                    print("Your content changed is successfully.")

        else:
            print("File does not exists.")

    except Exception as err:
        print(f"An error occured as {err}")

def delete_file():
    try:
        read_folder()
        name = input("Tell me file name which you want to delete with there extension: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("File is deleted successfully.")

        else:
            print("File does not exists.")

    except Exception as err:
        print(f"An error occured as {err}")


    
print("Options Guideline.\n")
print("1 : Create a folder.")
print("2 : Read files and folders.")
print("3 : Update the folder.")
print("4 : Delete the folder.\n")

print("5 : Create a file.")
print("6 : Read files.")
print("7 : Update the file.")
print("8 : Delete the file.")
print("0 : Exit the program.\n")



while True:
    try:
        choice = int(input("Choose Your Option: "))
        if choice < 0 or choice > 8:
            print("Invalid Input.")
            continue

    except ValueError:
        print("You put wrong input please enter a number.")
        continue

    if choice == 1:
        create_folder()

    elif choice == 2:
        read_folder()

    elif choice == 3:
        update_folder()

    elif choice == 4:
        delete_folder()

    elif choice == 5:
        create_file()

    elif choice == 6:
        read_file()

    elif choice == 7:
        update_file()

    elif choice == 8:
        delete_file()

    elif choice == 0:
        print("You successfully exit from program.")
        break

