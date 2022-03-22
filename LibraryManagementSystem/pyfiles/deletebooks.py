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
issued_table = "books_issued"


# Removes the book from the mysql database.
def deleteBook():
    book_id = book_info_1.get()

    delete_sql = "delete from " + book_table + " where bookid = '" + book_id + "'"
    delete_issue = "delete from " + issued_table + " where bookid = '" + book_id + "'"

    # Try to apply changes else show error box
    try:
        cursr.execute(delete_sql)
        connect_db.commit()
        cursr.execute(delete_issue)
        connect_db.commit()

        messagebox.showinfo("Success!", "Book record deleted.")

    except:
        messagebox.showinfo("Error", "Please check info and try again")

    book_info_1.delete(0, END)
    root.destroy()

# Creates window and labels for the delete page.
def delete():
    global book_info_1, book_info_2, book_info_3, book_info_4, canvas1, connect_db, book_table, root, cursr

    # Creating window
    root = Tk()
    root.title("Library System - Delete Book")
    root.minsize(width=400, height=400)
    root.maxsize(width=1000, height=800)
    root.geometry("800x700")
    canvas1 = Canvas(root)
    canvas1.config(bg="white")
    canvas1.pack(expand=True, fill=BOTH)

    # Create header with title
    header_frame = Frame(root, bg="#000d1a", bd=4)
    header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    header_label = Label(header_frame, text="Delete Book", bg="white", fg="#000d1a", font=("San Francisco", 16))
    header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Background for labels and input
    label_frame = Frame(root, bg="#99ccff")
    label_frame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

    # Label and input for book to be deleted
    label_deletion = Label(label_frame, text="Book ID : ", bg="white")
    label_deletion.place(relx=0.1, rely=0.5)
    book_info_1 = Entry(label_frame)
    book_info_1.place(relx=0.3, rely=0.5, relwidth=0.6)

    # Submit Button
    btn_submit = Button(root, text="Delete Book", bg="grey", command=deleteBook)
    btn_submit.place(relx=0.3, rely=0.8, relwidth=0.15, relheight=0.1)

    # Quit Button
    btn_quit = Button(root, text="Quit Page", bg="grey", command=lambda: root.destroy())
    btn_quit.place(relx=0.6, rely=0.8, relwidth=0.15, relheight=0.1)

    root.mainloop()
