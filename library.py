books = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    books.append({"name": name, "author": author})
    print("Book added successfully!")

def view_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book["name"], "-", book["author"])

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()
