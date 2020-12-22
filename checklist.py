from tkinter import *
#CHECKLIST FORM

checklist = Tk()
checklist.title("SLS Checklist")
checklist.geometry('300x300')

#FRAMES
frame = LabelFrame(checklist, text='Checklist')
frame.pack()

#LABELS
study_code =Label(frame,text='Study code')



#LABELS GRID

#BOXES
study_box = Entry(frame,width=30,borderwidth=5).pack()



#BOXES GRID



checklist.mainloop()