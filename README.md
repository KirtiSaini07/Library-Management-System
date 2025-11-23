# Library-Management-System
A simple Python-based Library Management System built using Object-Oriented Programming and file handling.
This project allows users to manage books, track issued/available status, and store records in a persistent text file.

**🔖 Project Overview**
The Library Inventory Manager is a command-line application that simulates a lightweight library system.
The project includes:
- A Book class for storing book details
- A LibraryInventory class for managing the book collection
- A menu-driven interface for interacting with the system
- Text-file–based storage (library.txt)
- Exception handling and logging for reliability
All functionalities are implemented inside a single file: library.py.

**🔖 Features**
- Book Management: Add new books
                   View all books
                   Search books by title or ISBN
- Issue & Return System: Issue a book (status changes to issued)
                         Return a book (status changes back to available)
- File Handling: All books are saved automatically to library.txt
                 Data is loaded at program start
- Error Handling: Handles missing files
                  Handles invalid inputs
                  Prevents issuing a book that is already issued
- Logging: Records operations and errors in library.log

 **🔖 Usage**
-Ensure library.py is in your project folder.
-Run the program using: python library.py
-Choose an option from the menu: 1.Add Book
                                 2.Issue Book
                                 3.Return Book
                                 4.View All Books
                                 5.Search Book
                                 6.Exit

All changes are saved automatically to library.txt.

**🔖 Output**


<img width="308" height="439" alt="output" src="https://github.com/user-attachments/assets/c8ecf2be-f9fb-47c3-a51c-b71aa1cb722a" />
