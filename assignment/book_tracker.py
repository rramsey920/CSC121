def dashboard():
    print("========================================")
    print("YOUR LIBRARY")
    print("========================================")

def estimate_reading_time(pages):
    #40pg/hr
    hours = round(pages/40, 1)
    return hours

def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    book = {"title": title, "author": author, "pages": pages, "hours": hours}
    library.append(book)

    print(f"Book added: '{title}' by {author} -- approx. {hours} hours to read")
    return library

def show_menu():
    print(f"""What would you like to do?
    1) View books
    2) Add a book

    q) Quit
    """)
    user = input("> ")

    user = user.strip().lower()
    return user

def view_books(library):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            print(i + 1,".", library[i])


def main():
    library = []
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

