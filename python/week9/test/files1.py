from typing import IO

def menu() -> str:
    print(
        "[1] Enter Student Details\n",
        "[2] Display Student Details\n",
        "[3] Exit Program\n",
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


while True:
    c = menu()
    if c == "1":
        f = open("students.txt", "a")
        enter_student_details(f)
    elif c == "2":
        f = open("students.txt", "r")
        display_student_details(f)
    elif c == "3":
        break
    else:
        print("Invalid choice! ")