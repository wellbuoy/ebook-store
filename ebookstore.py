#import necessary libraries
import sqlite3
import tabulate

# Establish connection with the database
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()


# Printing bookstore clerk menu
def display_menu():
    print("\nBOOKSTORE CLERK SYSTEM...")
    print("1 => Enter book")
    print("2 => Update book")
    print("3 => Delete book")
    print("4 => Search books")
    print("0 => Exit")

# Get all books from the database
all_books = cursor.execute("SELECT * FROM book").fetchall()
table_data = []
for row in all_books:
    table_data.append([row[0], row[1], row[2], row[3]])

#print the all the books from the data base in a table format
headers = ['id', 'title', 'author', 'qty']
tabulated_output = tabulate.tabulate(table_data, headers=headers, tablefmt="fancy_grid")
print("\n---------------------------------BOOK---------------------------------------")
print(tabulated_output)

# Infinite loop to continuously display the menu
while True:
    display_menu()
    choice = input("\nPlease enter your choice: ")
    
    # User choice 1: Add a new book
    if choice == '1':
        id = int(input("Please enter book id: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter book quantity: "))
        cursor.execute('INSERT INTO book VALUES (?, ?, ?, ?)', (id, title, author, qty))
        print("\nBook added successfully.")
    
    # User choice 2: Update book details
    elif choice == '2':
        id = int(input("Please enter book id: "))
        title = input("Enter new book title: ")
        author = input("Enter new book author: ")
        qty = int(input("Enter new book quantity: "))
        cursor.execute('UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?', (title, author, qty, id))
        print("\nBook updated successfully.")
    
    # User choice 3: Delete a book
    elif choice == '3':
        id = int(input("Please enter book id: "))
        cursor.execute('DELETE FROM book WHERE id = ?', (id,))
        print("\nBook deleted successfully.")

 # User choice 4: Search for a book
    elif choice == '4':
        id = int(input("Plase enter book id: "))
        cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
        result = cursor.fetchone()
        if result:
            print("\n----------BOOK FOUND!!-----------")
            print("ID        : ", result[0])
            print("Title     : ", result[1])
            print("Author    : ", result[2])
            print("Quantity  : ", result[3])
            print("---------------------------------")
        else:
            print("\nNo book found with this id.")
    
    # User choice 0: Exit the program
    elif choice == '0':
        print("\nGoodbye!!.")
        break
    
    #if the user enter invalid choice then it must print the error message in appropriate manner 
    else:
        print("\nInvalid choice. Please enter a valid choice.")

# Commit changes and close the connection
conn.commit()
conn.close()
