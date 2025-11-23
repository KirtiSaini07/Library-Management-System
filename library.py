'''
Name: Kirti Saini
Date: 23/11/2025
Title: Library Inventory Management System
'''

import logging
logging.basicConfig(filename="library.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

#--------------------  Book Class  ----------------------
class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}"
    
    def issue(self):
        if self.status == "Issued":
            print("Book already issued.")
        else:
            self.status = "Issued"
            print("Book issued successfully.")        

    def return_book(self):
        if self.status == "Available":
            print("Book is already available.")
        else:
            self.status = "Available"
            print("Book returned successfully.")        

    def is_available(self):
        return self.status == "Available"  

#--------------------  Inventory Class  ----------------------
class LibraryInventory:
    File='library.txt'

    def __init__(self):
        self.books = []   

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to inventory.")

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def search_by_isbn(self, isbn):
        found_books = [book for book in self.books if isbn.lower() in book.isbn.lower()]
        return found_books

    def display_all(self):
        if not self.books:
            print("No books in Library.")
        else:    
            for book in self.books:
                print(book) 
                
#--------------------  File Handling  ---------------------- 
def save_file(self):  
    with open(self.File, 'w') as f:
        try:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.isbn},{book.status}\n") 
        except Exception as e:
            logging.error(f"Saving file failed: {e}")  

def load_file(self):  
    try:
        with open(self.File, 'r') as f:
            for line in f:
                title, author, isbn, status = line.strip().split(',')
                book = Book(title, author, isbn, status)
                self.books.append(book)
    except FileNotFoundError:
        print("No existing inventory file found.") 
    except Exception as e:
        logging.error(f"Loading file failed: {e}") 

#--------------------  Main Program  ----------------------   
def menu():
    inventory = LibraryInventory()
    while True:
        print("\nLibrary Inventory Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        ch=input("Enter your choice: ")
        if ch=='1':
            title=input("Enter book title: ")
            author=input("Enter book author: ")
            isbn=input("Enter book ISBN: ")
            book=Book(title, author, isbn)
            inventory.add_book(book)
            inventory.save_file()

        elif ch=='2':
            isbn=input("Enter book ISBN to issue: ")
            found_books=inventory.search_by_isbn(isbn)
            if found_books:
                found_books[0].issue()
                inventory.save_file()
            else:
                print("Book not found.")

        elif ch=='3':
            isbn=input("Enter book ISBN to return: ")
            found_books=inventory.search_by_isbn(isbn)
            if found_books:
                found_books[0].return_book()
                inventory.save_file()
            else:
                print("Book not found.")

        elif ch=='4':
            inventory.display_all()

        elif ch=='5':
            search_choice=input("Search by (1) Title or (2) ISBN: ")
            if search_choice=='1':
                title=input("Enter book title to search: ")
                found_books=inventory.search_by_title(title)
            elif search_choice=='2':
                isbn=input("Enter book ISBN to search: ")
                found_books=inventory.search_by_isbn(isbn)
            else:
                print("Invalid choice.")
                continue

            if found_books:
                for book in found_books:
                    print(book)
            else:
                print("No books found.")

        elif ch=='6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

menu()
            