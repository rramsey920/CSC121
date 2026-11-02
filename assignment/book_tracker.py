import csv


def dashboard():
    print("========================================")
    print("YOUR LIBRARY")
    print("========================================")

#Main Menu
def show_menu():
    print(f"""What would you like to do?
    1) View books
    2) Add a book

    q) Quit
    """)
    user = input("> ")

    user = user.strip().lower()
    return user

#Option 2 - Adding book to library/csv
def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    book = {"title": title, "author": author, "pages": pages, "hours": hours}
    library.append(book)

    with open("books.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "pages", "hours"])
        writer.writerow({"title": title, "author": author, "pages": pages, "hours": hours})

    print(f"Book added: '{title}' by {author} -- approx. {hours} hours to read")
    return library

#Calculate reading time
def estimate_reading_time(pages):
    #40pg/hr
    hours = round(pages/40, 1)
    return hours

#Loading book from csv
def load_books():
    library = []

    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = ({"title": row["title"], "author": row["author"], "pages": int(row["pages"]), "hours": float(row["hours"])})
            library.append(book)
    return library

#Option 1 - prints library
def view_books(library):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            book = library[i]
            number = i + 1
            #print(i + 1, f". '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} hours to read)", sep="")
            print(format_book(book, number), sep="")

#Formats the input to be printed
def format_book(book, number):
    book_format = (f"{number}. '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} hours to read)")
    return book_format



def main():
    library = load_books()
    dashboard()
    while True:
        menu_choice = show_menu()
        if menu_choice == "1":
            view_books(library)

        elif menu_choice == "2":
            add_book(library)

        elif menu_choice == "q" or menu_choice == "quit" or menu_choice == "exit":
            print("Goodbye!")
            break

        else: 
            print("Sorry, that option isn't available.")
    


if __name__ == "__main__":
    main()

