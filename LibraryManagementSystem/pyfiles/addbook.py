from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Adds the book and accompanying info to the mysql book table
def registerBook():
    bookid = book_info_1.get()
    title = book_info_2.get()
    author = book_info_3.get()
    status = book_info_4.get()

    book_insert = "insert into " + book_table + " values('" + bookid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cursr.execute(book_insert)
        connect_db.commit()
        messagebox.showinfo("Success!", "The book has been added.")
    except:
        messagebox.showinfo("Error!", "Cannot add book to database.")

    # Destroy root frame after completing
    root.destroy()

# Creates frame, label and buttons so that the user can input information for adding a book
def addBook():
    global book_info_1, book_info_2, book_info_3, book_info_4, canvas1, connect_db, book_table, root, cursr

    # Creating window
    root = Tk()
    root.title("Library System - Add Book")
    root.minsize(width=400, height=400)
    root.maxsize(width=1000, height=800)
    root.geometry("800x700")

    # Connect to mysql
    my_password = "mypass123"
    my_database = "librarydb"
    connect_db = pymysql.connect(host="localhost",
                                 user="root",
                                 password="mypass123",
                                 database="librarydb")
    cursr = connect_db.cursor()

    # Name of table
    book_table = "books"
    canvas1 = Canvas(root)
    canvas1.config(bg="white")
    canvas1.pack(expand=True, fill=BOTH)

    # Create header with title
    header_frame = Frame(root, bg="#000d1a", bd=4)
    header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    header_label = Label(header_frame, text="Add Book", bg="white", fg="#000d1a", font=("San Francisco", 16))
    header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Background for labels and input
    label_frame = Frame(root, bg="#99ccff")
    label_frame.place(relx=0.15, rely=0.3, relwidth= 0.7 , relheight=0.4)

    # Book Id
    label_book_id = Label(label_frame,text="Book ID: ", bg="black", fg="white")
    label_book_id.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.1)
    book_info_1 = Entry(label_frame)
    book_info_1.place(relx= 0.3, rely= 0.2 , relwidth= 0.6, relheight=0.1)

    # Book Title
    label_title = Label(label_frame,text="Title: ", bg="black", fg="white")
    label_title.place(relx=0.1, rely=0.35, relheight=0.1, relwidth=0.1)
    book_info_2 = Entry(label_frame)
    book_info_2.place(relx= 0.3, rely= 0.35 , relwidth= 0.6, relheight=0.1)

    # Book Author
    label_author = Label(label_frame, text="Author: ", bg="black", fg="white")
    label_author.place(relx=0.1, rely=0.5, relheight=0.1, relwidth=0.1)
    book_info_3 = Entry(label_frame)
    book_info_3.place(relx=0.3, rely=0.5, relwidth=0.6, relheight=0.1)

    # Book Status
    label_status = Label(label_frame, text="Status: ", bg="black", fg="white")
    label_status.place(relx=0.1, rely=0.65, relheight=0.1, relwidth=0.1)
    book_info_4 = Entry(label_frame)
    book_info_4.place(relx=0.3, rely=0.65, relwidth=0.6, relheight=0.1)

    # Submit Button
    btn_submit = Button(root, text="Submit Book", bg="grey",  command=lambda:registerBook())
    btn_submit.place(relx=0.3, rely=0.8, relwidth=0.15, relheight=0.1)

    # Quit Button
    btn_quit = Button(root, text="Quit Page", bg="grey", command=lambda:root.destroy())
    btn_quit.place(relx=0.6, rely=0.8, relwidth=0.15, relheight=0.1)


    root.mainloop()