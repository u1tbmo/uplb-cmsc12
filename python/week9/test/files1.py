from typing import IO
import os


file_dir = os.path.dirname(__file__)
file_path = os.path.join(file_dir, "students.txt")


def menu() -> str:
    print(
        "[1] Enter Student Details\n",
        "[2] Display Student Details\n",
        "[3] Edit Student Details\n",
        "[4] Exit Program\n",
        sep=""
    )
    return input("Enter your choice: ")


def enter_student_details(file_to_write: IO[str]) -> None:
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    file_to_write.write(f"{name},{age}\n")
    file_to_write.close()


def display_student_details(file_to_read: IO[str]) -> None:
    print(
            "Name                  Age\n"
            "========================="
        )
    for line in file_to_read:
        name, age = line.split(",")
        print(f"{name:<20}{age:>5}",end="")

    print("=========================")

    file_to_read.close()


def edit_student_details(file_to_edit: IO[str]) -> None:
    file_lines = file_to_edit.readlines()
    
    edit_name = input("Enter student name to edit: ")
    edit_age = input("Enter the student's age: ")

    for i,l in enumerate(file_lines):
        name, age = l.split(",")
        age = age.rstrip()
        if name == edit_name and age == edit_age:
            print("Student found!")
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")

            file_lines[i] = f"{new_name},{new_age}\n"
            break
    else:
        print("Student not found!")
        file_to_edit.close()
        return
    
    file_to_edit.close()

    file_to_edit = open(file_path, "w")
    for line in file_lines:
        file_to_edit.write(line)

    
    file_to_edit.close()
    

while True:
    c = menu()
    if c == "1":
        f = open(file_path, "a")
        enter_student_details(f)
    elif c == "2":
        f = open(file_path, "r")
        display_student_details(f)
    elif c == "3":
        f = open(file_path, "r+")
        edit_student_details(f)
    elif c == "4":
        break
    else:
        print("Invalid choice! ")