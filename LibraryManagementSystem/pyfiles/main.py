from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
import os
# import pymysql.cursors
from tkinter import messagebox
from addbook import *
from deletebooks import *
from viewbooks import *
from issuebook import *
from returnbooks import *

# Connecting to MySql server
my_password = "mypass123"
my_database = "librarydb"
connect_db = pymysql.connect(host="localhost",
                             user="root",
                             password="mypass123",
                             database="librarydb")
cursr = connect_db.cursor()

# Creating window frame
root = Tk()
root.title("Library System")
root.minsize(width=400, height=400)
root.maxsize(width=1000, height=800)
root.geometry("800x700")

# Adding and setting background image
same = True
n = 0.25

# Find the image by getting the directory, slicing it and adding location
path = os.path.dirname(__file__)
path_mod = path[:-7]
my_file = path_mod + 'images/bookimage.jpg'

background_img = Image.open(my_file)
[img_width, img_height] = background_img.size

# Adjusting the image dimensions
new_img_width = int(img_width * n)
if same:
    new_img_height = int(img_height * n)
else:
    new_img_height = int(img_height / n)

background_img = background_img.resize((new_img_width, new_img_height))
canvas1 = Canvas(root)
bg_image = ImageTk.PhotoImage(background_img)
canvas1.create_image(400, 400, image=bg_image)
canvas1.config(bg="black", width=new_img_width, height=new_img_height)
canvas1.pack(expand=True, fill=BOTH)

# Create header with title
header_frame = Frame(root, bg="#000d1a", bd=4)
header_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
header_label = Label(header_frame, text="Welcome to the Library System", bg="white", fg="#000d1a",
                     font=("San Francisco", 16))
header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons
btn_addbook = Button(root, text="Add Book", bg="white", fg="#000d1a", font=("San Francisco", 12), command=addBook)
btn_addbook.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

btn_deletebook = Button(root, text="Delete Book", bg="white", fg="#000d1a", font=("San Francisco", 12), command=delete)
btn_deletebook.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

btn_viewbook = Button(root, text="View Book", bg="white", fg="#000d1a", font=("San Francisco", 12), command=bookView)
btn_viewbook.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)

btn_issuebook = Button(root, text="Issue Book", bg="white", fg="#000d1a", font=("San Francisco", 12), command=issueBook)
btn_issuebook.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)

btn_returnbook = Button(root, text="Return Book", bg="white", fg="#000d1a", font=("San Francisco", 12),
                        command=returnBook)
btn_returnbook.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

root.mainloop()
