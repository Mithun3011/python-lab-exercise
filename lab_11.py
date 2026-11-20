
# Log File Reader

filename = input("Enter file name: ")

try:
    file = open(filename, "r")

    print("\n--- LOG FILE CONTENTS ---")

    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("File not found!")
