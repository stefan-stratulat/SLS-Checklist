from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from checklist import frames


root = Tk()
root.title("SLS Checklist")
root.iconbitmap('images/fire_eye_alien.ico')
root.configure(bg="#add8e6")
root.geometry('250x300')



"""Button to add a new study, will open the frames function from checklist module"""
add_study = Button(root, text="Add new study", command= frames,padx=10, pady=10)

#Search label that will search on the database for the study code.
search_label = Label(root, text="Search study code",bg="#add8e6")
search_box = Entry(root,width=30)

#Grid
add_study.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
search_label.grid(row=1,column=0)
search_box.grid(row=2,column=0, pady=10,ipady=10)



root.mainloop()

