
# Library Management System

books = []

while True:
    print("\n--- LIBRARY MANAGEMENT ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added!")

    elif choice == "2":
        print("\n--- BOOK LIST ---")

        if len(books) == 0:
            print("No books available!")
        else:
            for book in books:
                print(book)

    elif choice == "3":
        book = input("Enter book to borrow: ")

        if book in books:
            books.remove(book)
            print("Book borrowed!")
        else:
            print("Book not available!")

    elif choice == "4":
        book = input("Enter book to return: ")

        books.append(book)
        print("Book returned!")

    elif choice == "5":
        print("Library system closed!")
        break

    else:
        print("Invalid choice!")
