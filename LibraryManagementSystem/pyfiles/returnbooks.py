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
all_book_id = []


def returnB():
    global btn_return, btn_quit, canvas1, connect_db, root, label_frame, label_return_1, return_info_1, status

    book_id = return_info_1.get()
    print(book_id)
    extracted_book_id = "select bookid from " + issued_table
    print(extracted_book_id)

    try:
        cursr.execute(extracted_book_id)
        connect_db.commit()
        for i in cursr:
            all_book_id.append(i[0])

        if book_id in all_book_id:
            print("pass")
            check_avail = "select status from " + book_table + " where bookid = '" + book_id + "'"
            cursr.execute(check_avail)
            connect_db.commit()
            for i in cursr:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error!", "Book ID is not present")
    except:
        messagebox.showinfo("Error!", "Cannot find Book ID")

    issue_to_sql = "delete from " + issued_table + " where bookid = '" + book_id + "'"

    update_status = "update " + book_table + " set status = 'avail' where bookid = '" + book_id + "'"

    try:
        if book_id in all_book_id and status == True:
            cursr.execute(issue_to_sql)
            connect_db.commit()
            cursr.execute(update_status)
            connect_db.commit()
            messagebox.showinfo("Success", "Book returned Successfully")
        else:
            all_book_id.clear()
            messagebox.showinfo("Error", "please check book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Error!", "The input you have entered is incorrect, try again")

    all_book_id.clear()
    root.destroy()


def returnBook():
    global return_info_1, btn_return, btn_quit, canvas1, connect_db, cursr, root, label_frame, label_return_1
    # Creating window
    root = Tk()
    root.title("Library System - Return Book")
    root.minsize(width=400, height=400)
    root.maxsize(width=1000, height=800)
    root.geometry("800x700")

    canvas1 = Canvas(root)
    canvas1.config(bg="white")
    canvas1.pack(expand=True, fill=BOTH)

    # Create header with title
    header_frame = Frame(root, bg="#000d1a", bd=4)
    header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    header_label = Label(header_frame, text="Return Book", bg="white", fg="#000d1a", font=("San Francisco", 16))
    header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Background for labels and input
    label_frame = Frame(root, bg="#99ccff")
    label_frame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

    # Book ID to return
    label_return_1 = Label(label_frame, text="Book ID : ", bg="white")
    label_return_1.place(relx=0.1, rely=0.3)
    return_info_1 = Entry(label_frame)
    return_info_1.place(relx=0.3, rely=0.3, relwidth=0.6)

    # Return Button
    btn_return = Button(root, text="Return Book", bg="grey", command=returnB)
    btn_return.place(relx=0.3, rely=0.8, relwidth=0.15, relheight=0.1)

    # Quit Button
    btn_quit = Button(root, text="Quit Page", bg="grey", command=lambda: root.destroy())
    btn_quit.place(relx=0.6, rely=0.8, relwidth=0.15, relheight=0.1)

    root.mainloop()
