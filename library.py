from books import Book
from members import Member
from typing import Dict

class Library:
    def __init__(self):
        self.membership_id = 0                  # Temp dummy membership id
        self.day = 0                            # Temp dummy day instead of date format
        self.books: Dict[int, Book] = dict()
        self.members: Dict[int, Member] = dict()
        self.dues: Dict[int, Dict[int, int]] = dict()    
        # dues are stored as {isbn_of_book : {membership_id: due_date}}

    # ------------------- Book -------------------
    
    # Given the necessary details of a book, adds it to the library
    def add_book(self, isbn, title, author, genre):
        book = Book(ISBN=isbn, 
                    title=title, 
                    author=author, 
                    genre=genre)
        self.books[isbn] = book
        print(f"Added book `{title}` successfully! (isbn: {isbn})")
    
    # Removes a book from the library using the isbn
    def remove_book(self, isbn):
        book = self.books.pop(isbn)
        print(f"Removed book `{book.title}` successfully! (isbn: {isbn})")
    
    # Given the details of a book, updates the details of the book
    def update_book_details(self, isbn, key, value):
        self.books[isbn].update_book(key, value)

    def get_all_books(self):
        return list(self.books.values())
    
    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            if genre and genre.lower() not in book.genre.lower():
                continue
            results.append(book)
        return results


    # ------------------- Member -------------------

    # Given the details of a member, adds it to the library
    def add_member(self, name, contact):
        member = Member(membership_id=self.membership_id,
                        name=name,
                        contact=contact)
        self.members[self.membership_id] = member
        print(f"Added member successfully! (membership_id: {self.membership_id})")
        self.membership_id += 1

    # Removes a member from the library using the membership id
    def remove_member(self, membership_id):
        member = self.members.pop(membership_id)
        print(f"Removed member successfully! (membership_id: {self.membership_id})")
        return member

    # A Member borrows a book, requires the membership id and isbn
    # and quantity of book decreases
    # The book is borrowed for Maximum of 10 days from today
    def borrow_book(self, membership_id, isbn):
        if self.books[isbn].quantity > 0:
            due_date = self.day + 10
            self.members[membership_id].borrow_book(due_date, isbn)
            if isbn not in self.dues:
                self.dues[isbn] = {}
            self.dues[isbn][membership_id] = due_date
            self.books[isbn].quantity -= 1
        else:
            print(f"Book title: {self.books[isbn].title} (isbn: {isbn}) is currently not available")

    # A Member returns a book, requires the membership id and isbn
    # quantity of book increases
    def return_book(self, membership_id, isbn):
        due_date = self.members[membership_id].return_book(isbn)
        if due_date < self.day:
            print(f"Its is Late, today it's {self.day} and the due date is {due_date}")
        
        self.dues[isbn].pop(membership_id)
        self.books[isbn].quantity += 1

    def get_all_members(self):
        return list(self.members.values())
    
    def update_member_details(self, membership_id, key, value):
        self.members[membership_id].update_member(key, value)

    # ------------------- Date and dues -------------------

    def increment_day(self):
        self.day += 1
        dues_today = []
        for isbn in self.dues.keys():
            for membership_id in self.dues[isbn].keys():
                if self.dues[isbn][membership_id] == self.day:
                    dues_today.append((membership_id, isbn))
        
        return self.day, dues_today
        
        