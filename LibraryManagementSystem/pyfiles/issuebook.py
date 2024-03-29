from tkinter import *
from PIL import ImageTk,Image
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

# Takes user and book id and adds it to issued book table if available
def issue():
    global btn_issue, label_frame, label_issue_1, issue_info_1, label_issue_2, issue_info_2, btn_quit, root, canvas1, status

    bookid = issue_info_1.get()
    issued_to = issue_info_2.get()

    btn_issue.destroy()
    label_frame.destroy()
    label_issue_1.destroy()
    issue_info_1.destroy()
    issue_info_2.destroy()

    extracted_book_id = "select bookid from " +book_table
    # Try to look through book database to see if book is available, if yes status true, else false
    try:
        cursr.execute(extracted_book_id)
        connect_db.commit()
        for i in cursr:
            all_book_id.append(i[0])
        if bookid in all_book_id:
            check_available = "select status from "+book_table+" where bookid = '"+bookid+"'"
            cursr.execute(check_available)
            connect_db.commit()
            for i in cursr:
                check = i[0]

            if check == "avail":
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID is not present")
    except:
        messagebox.showinfo("Error", "Cannot find books ID")

    issued_sql = "insert into " +issued_table+" values ('"+bookid+"','"+issued_to+"')"
    show = "select * from " + issued_table

    update_status = "update " +book_table+" set status = 'issued' where bookid = '"+bookid+"'"

    # Try, if book is in book collection and status is true update issued book table with book id and user
    try:
        if bookid in all_book_id and status == True:
            cursr.execute(issued_sql)
            connect_db.commit()
            cursr.execute(update_status)
            connect_db.commit()
            messagebox.showinfo("Success!", "Book has been issued successfully")
            root.destroy()
        else:
            all_book_id.clear()
            messagebox.showinfo("Sorry", "This book has already been issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Error!", "Entered the wrong details, please try again" )

    all_book_id.clear()





# Creates window and labels for the issue page.
def issueBook():
    global btn_issue, label_frame, label_issue_1,issue_info_1, label_issue_2,issue_info_2,btn_quit,root,canvas1,status

    # Creating window
    root = Tk()
    root.title("Library System - Issue Books")
    root.minsize(width=400, height=400)
    root.maxsize(width=1000, height=800)
    root.geometry("800x700")

    canvas1 = Canvas(root)
    canvas1.config(bg="white")
    canvas1.pack(expand=True, fill=BOTH)

    # Create header with title
    header_frame = Frame(root, bg="#000d1a", bd=4)
    header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    header_label = Label(header_frame, text="Issue Book", bg="white", fg="#000d1a", font=("San Francisco", 16))
    header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Background for labels and input
    label_frame = Frame(root, bg="#99ccff")
    label_frame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

    # Book ID
    label_issue_1 = Label(label_frame,text="Book ID : ", bg="white")
    label_issue_1.place(relx=0.1, rely=0.3)
    issue_info_1 = Entry(label_frame)
    issue_info_1.place(relx=0.3,rely=0.3, relwidth=0.6)

    # Issued to Name
    label_issue_2 = Label(label_frame,text="Issued to : ", bg="white")
    label_issue_2.place(relx=0.1,rely=0.6)
    issue_info_2 = Entry(label_frame)
    issue_info_2.place(relx=0.3,rely=0.6,relwidth=0.6)

    # Issue Button
    btn_issue = Button(root, text="Issue Book", bg="grey", command=lambda: issue())
    btn_issue.place(relx=0.3, rely=0.8, relwidth=0.15, relheight=0.1)

    # Quit Button
    btn_quit = Button(root, text="Quit Page", bg="grey", command=lambda: root.destroy())
    btn_quit.place(relx=0.6, rely=0.8, relwidth=0.15, relheight=0.1)

    root.mainloop()