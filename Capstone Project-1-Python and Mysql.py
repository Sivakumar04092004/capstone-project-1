# Capstone Project-1- Application using Python Libraries and DB

# Project- Library Management System

    # 1. Add book information
    # 2. Display book information
    # 3. To list all books of a given author
    # 4. To list the count of books in the library
    # 5. Exit


import pymysql  # python + mysql = pymysql

lms = pymysql.connect(host='localhost', user='root', password='root123',database='anna_centenary_library_chennai')  # Connect to the database

cursor = lms.cursor()

sql = '''                                     # Table creation
create table books_info (
    book_id INT(10) PRIMARY KEY,
    title VARCHAR(50),
    author VARCHAR(50),
    type_of_book VARCHAR(30),
    public_name VARCHAR(40),
    edition INT(20),
    pages INT(10),
    price INT(10)
)
'''

try:
    cursor.execute(sql)
    print("Table created successfully")
except pymysql.MySQLError as e:
    print(f"Error creating table: {e}")

lms.close()     # Close the connection


# 1. Add book information

import pymysql

lms = pymysql.connect(host='localhost', user='root', password='root123', database='anna_centenary_library_chennai')

def add_book(book_id, title, author, type_of_book, public_name, edition, pages, price):
    try:
        with lms.cursor() as cursor:
            query = 'insert into books_info (book_id, title, author, type_of_book, public_name, edition, pages, price) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(query, (book_id, title, author, type_of_book, public_name, edition, pages, price))
        lms.commit()
        print("Book added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        
lms.close()

# 2. Display book information


import pymysql

lms = pymysql.connect(host='localhost', user='root', password='root123', database='anna_centenary_library_chennai')


def display_books():
    with lms.cursor() as cursor:
        query = 'select * from books_info'
        cursor.execute(query)
        complete = cursor.fetchall()

        for row in complete:
            print(row)


lms.close()


# 3. To list all books of a given author

import pymysql

lms = pymysql.connect(host='localhost', user='root', password='root123', database='anna_centenary_library_chennai')

def book_author(author):
    try:
        with lms.cursor() as cursor:
            query = 'select * from books_info where author = %s'
            cursor.execute(query, (author,))
            complete = cursor.fetchall()

            for row in complete:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

lms.close()


# 4. To list the count of books in the library

import pymysql

lms = pymysql.connect( host='localhost', user='root', password='root123', database='anna_centenary_library_chennai')

def count_books():
    with lms.cursor() as cursor:
        query = 'select count(*) from books_info'
        cursor.execute(query)
        complete = cursor.fetchone()  

        print(f'Total number of Books: {complete[0]}')

lms.close()


# Main menu

import pymysql

lms = pymysql.connect(host='localhost', user='root', password='root123', database='anna_centenary_library_chennai')

def main():
    while True:
        print('\nLibrary Management System:')
        print("1. Add book information")
        print("2. Display book information")
        print("3. List all books of a given author")
        print("4. Count books in the library")
        print("5. Exit")

        step = input("Enter your choice: ")

        if step == '1':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            type_of_book = input("Enter Type of Book: ")
            public_name = input("Enter Publication Name: ")
            edition = int(input("Enter Year of Publication: "))
            pages = int(input("Enter Pages: "))
            price = int(input("Enter Price of Book: "))
            add_book(book_id, title, author, type_of_book, public_name, edition, pages, price)

        elif step == '2':
            display_books()

        elif step == '3':
            author = input("Enter Author Name: ")
            book_author(author)

        elif step == '4':
            count_books()

        elif step == '5':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


lms.close()

