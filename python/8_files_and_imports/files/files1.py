"""Demo for files."""
import os

# Ensures that the file being saved to is always next to the python file.
file_dir = os.path.dirname(__file__)
file_path = os.path.join(file_dir, "data.dat")

def menu():
    print("[1] Write",
          "[2] Read ",
          "[3] Exit ",
          end="\n", sep="\n"
          )
    return input("Enter choice: ")

def write(f):
    num = int(input("Enter number of students: "))
    for i in range(num):
        name = input(f"{[i+1]} Enter name: ")
        f.write(name+"\n")

    f.close()

def read(f):
    for line in f:
        print(line, end="")

    f.close()

while True:
    c = menu()
    if c == "1":
        f = open(file_path, "w")
        write(f)
    elif c == "2":
        f = open(file_path, "r")
        read(f)
    elif c == "3":
        break
    else:
        print("Invalid choice.")

