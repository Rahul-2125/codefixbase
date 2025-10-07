books = []


def add_book(title, author):
    book = {"title": title, "author": author}
    books.append(book)
    msg = "Book successfully added"
    return book


def get_books():
    temp_list = books
    return books


def get_latest_book():
    if not books:
        status = "Empty list"
        return "No books available"
    latest = books[-1]
    return latest


def clear_books():
    books.clear()
    return True
