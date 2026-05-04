#part2
class Book:
    library_name = "City Central Library"

    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            print(f"You have checked out {self.title}")
        else:
            print(self.title, "is already checked out.")

    def return_book(self):
        self.is_available = True
        print(self.title, "has been returned.")

    def display_info(self):
        print("-------- Book Info --------")
        print("Title:", self.title)
        print("Author:", self.author)
        # if self.is_available:
        #     print("Status: Available")
        # else:
        #     print("Status: Checked Out")
        status = "Available" if self.is_available else "Checked Out"
        print(f"Status: {status}")
        print(f"Library: {self.library_name}") # Accessing class property
        print("----------------------")

#part3
book1 = Book("Harry Potter", "J.K. Rowling", "1111")
book2 = Book("Percy Jackson", "Rick Riordan", "2222")

print(book1.library_name)
print(book2.library_name)
print("----------------------")

book1.display_info()
book1.checkout()
book1.checkout()

print("----------------------")
# Test return logic
book1.return_book()
book1.display_info()

# Bonus: Update class property for all instances
Book.library_name = "Metropolitan Library"
print(book2.library_name) # Will now show "Metropolitan Library"

# STACK
from collections import deque

stack = deque()

# Push
stack.append(1)
stack.append(2)

# Pop
stack.pop() # Returns 2

# Check if empty
is_empty = len(stack) == 0





# QUEUE
from collections import deque

queue = deque()

# ENQUEUE: Use .append()
queue.append("First")
queue.append("Second")

# DEQUEUE: Use .popleft()
# This is O(1) - extremely fast!
served = queue.popleft() 
print(served) # "First"

