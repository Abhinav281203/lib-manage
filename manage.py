from library import Library

library = Library()

def add_book(isbn: int, title: str, author: str, genre: str):
    library.add_book(isbn=isbn, title=title, author=author, genre=genre)

def remove_book(isbn: int):
    library.remove_book(isbn=isbn)

def update_book_details(isbn: int, key: str, value: str):
    library.update_book_details(isbn=isbn, key=key, value=value)

def get_available_books():
    books = library.get_all_books()
    for book in books:
        status = "available" if book.quantity > 0 else "unavailable"
        print(f"`{book.title}` by {book.author} (genre: {book.genre}) | status: {status}")

def search_books(title: str = None, author: str = None, genre: str = None):
    books = library.search_books(title=title, author=author, genre=genre)
    print(f"Found {len(books)} books:")
    for book in books:
        status = "available" if book.quantity > 0 else "unavailable"
        print(f"`{book.title}` by {book.author} (genre: {book.genre}) | status: {status}")

def add_member(name: str, contact: str):
    library.add_member(name=name, contact=contact)

def remove_member(membership_id: int):
    library.remove_member(membership_id=membership_id)

def update_member_details(membership_id: int, key: str, value: str):
    library.update_member_details(membership_id=membership_id, key=key, value=value)

def get_all_members():
    members = library.get_all_members()
    for member in members:
        print(f"membership_id: {member.membership_id}, name: {member.name}, contact: {member.contact}")

def borrow_book(membership_id: int, isbn: int):
    library.borrow_book(membership_id=membership_id, isbn=isbn)

def return_book(membership_id: int, isbn: int):
    library.return_book(membership_id=membership_id, isbn=isbn)

def increment_day_and_get_dues():
    day, dues = library.increment_day()
    print(f"Day: {day}")
    if dues:
        print("Books due today:")
        for membership_id, isbn in dues:
            print(f"Name: {library.members[membership_id].name}, id: {membership_id}, Book: {library.books[isbn].title} (isbn: {isbn})")
