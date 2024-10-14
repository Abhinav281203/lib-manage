class Book:
    def __init__(self, 
                 ISBN: int, 
                 title: str, 
                 author: str, 
                 genre: str,
                 quantity: int = 10):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
            
    # Updates a book's details 
    # Need to specify which attribute to update and the new value
    def update_book(self, key, value):
        setattr(self, key, value)
        print(f"Updated `{self.title}` (isbn:{self.ISBN}) book details successfully! {key} -> {value}")
