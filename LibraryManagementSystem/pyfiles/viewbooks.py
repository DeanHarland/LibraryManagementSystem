from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Connect to mysql
my_password = "mypass123"
my_database = "librarydb"
connect_db = pymysql.connect(host="localhost",
                             user="root",
                             password="mypass123",
                             database="librarydb")
cursr = connect_db.cursor()
book_table = "books"

# Creates window and labels with database info to showcase the books.
def bookView():
    # Creating window
    root = Tk()
    root.title("Library System - View Books")
    root.minsize(width=400, height=400)
    root.maxsize(width=1000, height=800)
    root.geometry("800x700")

    canvas1 = Canvas(root)
    canvas1.config(bg="white")
    canvas1.pack(expand=True, fill=BOTH)

    # Create header with title
    header_frame = Frame(root, bg="#000d1a", bd=4)
    header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    header_label = Label(header_frame, text="View Books", bg="white", fg="#000d1a", font=("San Francisco", 16))
    header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Background for labels
    label_frame = Frame(root, bg="#99ccff")
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # rely= variable to iterate over
    y = 0.3

    # Create label and align text along
    Label(label_frame, text='{:<20} {:<60} {:<40} {:<20}'.format("bookID", "Title", "Author", "Status")
          , bg="white").place(relx=0.05, rely=0.1)

    Label(label_frame,
          text="------------------------------------------------------------------------------------------------",
          bg="white").place(relx=0.05, rely=0.19)

    # Get all books from book table and for each book add label with books info to a new line. Else error message.
    get_books = "select * from " + book_table
    try:
        cursr.execute(get_books)
        connect_db.commit()
        for i in cursr:
            Label(label_frame, text='{:<20} {:40.40} {:40.40} {:20.20}'.format(i[0], i[1], i[2], i[3],), bg="white").place(relx=0.05,
                                                                                                          rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to retrieve books from database")

    # Quit Button
    btn_quit = Button(root, text="Quit Page", bg="grey", command=lambda: root.destroy())
    btn_quit.place(relx=0.6, rely=0.8, relwidth=0.15, relheight=0.1)

    root.mainloop()