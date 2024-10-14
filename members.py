class Member:
    def __init__(self, 
                 membership_id: int,
                 name: str, 
                 contact: str, 
                ):
        self.membership_id = membership_id
        self.name = name
        self.contact = contact
        self.borrowed_books = {}
        # Stored as {isbn of book: due_date}
    
    # Update member details
    # Need to specify which attribute to update and the new value
    def update_member(self, key, value):
        setattr(self, key, value)

    # Borrow a book
    def borrow_book(self, due_day, isbn):
        self.borrowed_books[isbn] = due_day
        print(f"Borrowed book successfully! (membership_id: {self.membership_id}, isbn: {isbn} due_day: {due_day})")

    # Return a book
    def return_book(self, isbn):
        due_date = self.borrowed_books[isbn]
        self.borrowed_books.pop(isbn)
        print(f"Returned book successfully! (membership_id: {self.membership_id}, isbn: {isbn} due_day: {due_date})")
        return due_date