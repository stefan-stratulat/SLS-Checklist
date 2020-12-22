from tkinter import *
#CHECKLIST FORM

checklist = Tk()
checklist.title("SLS Checklist")
checklist.geometry('300x300')

#FRAMES
frame_1 = LabelFrame(checklist, text='Awarded Study')
frame_1.pack()

#LABELS
"""Awardeded Study frame labels """
awarded_study = Label(frame_1,text='Awarded Study')
internal_kom =Label(frame_1,text='Internal KOM')
check_wf = Label(frame_1, text="Check WF")
sls_task = Label(frame_1, text="Assign SLS in WF")
draft_lp = Label(frame_1, text="Draft loc. plan")


#LABELS GRID
awarded_study.grid(row=0,column=0, columnspan=2, padx=10, pady=10)
internal_kom.grid(row=1,column=0, padx=10)
check_wf.grid(row=2,column=0, padx=10)
sls_task.grid(row=3,column=0, padx=10)
draft_lp.grid(row=4,column=0, padx=10)

#BOXES
"""Awardeded Study frame boxex"""
internal_kom =Entry(frame_1, width=30)
check_wf = Entry(frame_1, width=30)
sls_task = Entry(frame_1, width=30)
draft_lp = Entry(frame_1, width=30)


#BOXES GRID

internal_kom.grid(row=1,column=1,padx=10)
check_wf.grid(row=2,column=1,padx=10)
sls_task.grid(row=3,column=1,padx=10)
draft_lp.grid(row=4,column=1,padx=10)


#BOXES GRID



checklist.mainloop()