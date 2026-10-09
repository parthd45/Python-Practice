#create a dictionary for library and check if a book is available or not
library = {
    "Book4": 5,
    "Book3": 3,
    "Book2": 2,
    "Book1": 4
}

#check if book is available or not
book_name = input("Enter the name of the book you want to check: ")
if book_name in library:
    print(f"The book '{book_name}' is available. Number of copies: {library[book_name]}")
else:
    print(f"The book '{book_name}' is not available.")