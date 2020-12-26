from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from checklist import frames


root = Tk()
root.title("SLS Checklist")
root.iconbitmap('images/fire_eye_alien.ico')
root.configure(bg="#add8e6")
root.geometry('500x300')

def show():
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()

    #Query the database
    c.execute("SELECT oid,* FROM studies")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0])+ " "+str(record[2]) +"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=1, column=3, columnspan=2,rowspan=30)

    conn.commit()
    conn.close()

#fuction for the update button, which will open the checklist with the data from the DB
# def update():
#     frames()
#     conn = sqlite3.connect('studies.db')
#     c = conn.cursor()
#     c.execute("Se")


#     conn.commit()
#     conn.close()


"""Button to add a new study, will open the frames function from checklist module"""
add_study = Button(root, text="Add new study", command=frames, padx=10, pady=5)
show_studies = Button(root, text="Show studies",command=show,padx=10, pady=5)
update_study = Button(root, text="Update study",padx=10, pady=5)

#Search label that will search on the database for the study code.
search_label = Label(root, text="Search study code",bg="#add8e6")
search_box = Entry(root,width=35)

#Grid
add_study.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
search_label.grid(row=1,column=0)
search_box.grid(row=2,column=0, padx=10, pady=10)
show_studies.grid(row=0,column=3,columnspan=2,padx=10,pady=5,ipadx=50)
update_study.grid(row=4,column=0,columnspan=2,padx=10,pady=5,ipadx=50)


root.mainloop()

