def dashboard():
    print("========================================")
    print("YOUR LIBRARY")
    print("========================================")

def estimate_reading_time(pages):
    #40pg/hr
    hours = round(pages/40, 1)
    return hours

def add_book():
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)
    print(f"'{title}' by {author} -- approx. {hours} hours to read")

def main():
    dashboard()
    add_book()

if __name__ == "__main__":
    main()

