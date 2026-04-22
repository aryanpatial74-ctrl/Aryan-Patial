books = [
    "Pride and Prejudice – Jane Austen",
    "Jane Eyre – Charlotte Brontë",
    "Wuthering Heights – Emily Brontë",
    "Great Expectations – Charles Dickens",
    "Crime and Punishment – Fyodor Dostoevsky",
    "War and Peace – Leo Tolstoy",
    "The Odyssey – Homer",
    "The Iliad – Homer",
    "The Divine Comedy – Dante Alighieri",
    "Don Quixote – Miguel de Cervantes",

    "To Kill a Mockingbird – Harper Lee",
    "1984 – George Orwell",
    "Animal Farm – George Orwell",
    "Brave New World – Aldous Huxley",
    "The Catcher in the Rye – J.D. Salinger",
    "Fahrenheit 451 – Ray Bradbury",
    "The Great Gatsby – F. Scott Fitzgerald",
    "Of Mice and Men – John Steinbeck",
    "The Grapes of Wrath – John Steinbeck",
    "Lord of the Flies – William Golding",

    "The Hobbit – J.R.R. Tolkien",
    "The Lord of the Rings – J.R.R. Tolkien",
    "Harry Potter and the Philosopher’s Stone – J.K. Rowling",
    "Harry Potter and the Deathly Hallows – J.K. Rowling",
    "A Game of Thrones – George R.R. Martin",
    "Dune – Frank Herbert",
    "Ender’s Game – Orson Scott Card",
    "The Lion
]
issued_books = ["The Midnight Library",
    "Sapiens: A Brief History of Humankind",
    "Educated"]


def add_book():
    name = input("Enter book name : ")
    books.append(name)
    print(name, "added")


def show_book():
    if len(books) == 0:
        print("No books Avaliable")
    else:
        print(books)
    for i in books:
        print(i)


def issue_book():
    if len(books) == 0:
        print("No books avaliable")
    else:
        show_book()
        name = input("Enter the book anme :")
        if name in books:
            books.remove(name)
            issued_books.append(name)
            print(name, "book issued")


def return_book():
    name = input("Enter book name you want to return :")
    if name is issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name, "Book returned")
    else:
        print(name, "book was not issued")


def library():
    while True:
        print("\n----menu----")
        print("1.Add Book")
        print("2.Show Books")
        print("3 Issue Book")
        print("4.Return Book")
        print("5.Exit")
        choice = int(input("\nEnter your choice : "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid choice")


library()
