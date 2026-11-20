
# Student Data Manager

while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        mark = input("Enter student mark: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + mark + "\n")

        print("Student details saved!")

    elif choice == "2":
        print("\n--- STUDENT RECORDS ---")

        try:
            with open("students.txt", "r") as file:
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("No student records found!")

    elif choice == "3":
        print("Program closed!")
        break

    else:
        print("Invalid choice!")
