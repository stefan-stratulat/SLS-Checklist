from tkinter import *
#CHECKLIST FORM

checklist = Tk()
checklist.title("SLS Checklist")
checklist.geometry('600x300')


#Study info
sponsor = Label(checklist, text="Sponsor")
sponsor.grid(row=0,column=3,pady=(10,0))
study_code = Label(checklist, text="Study Code")
study_code.grid(row=1,column=3,pady=(10,0))
sponsor_box = Entry(checklist,width=20)
sponsor_box.grid(row=0,column=4, pady=(10,0))
study_code_box = Entry(checklist,width=20)
study_code_box.grid(row=1,column=4,pady=(10,0))

#Checklist FRAMES
frame_1 = LabelFrame(checklist) #Awarded study frame
frame_1.grid(row=2,column=0,columnspan=2,pady=10)
frame_2 = LabelFrame(checklist) #Localisation setup frame
frame_2.grid(row=2,column=3,columnspan=2,pady=10)
frame_3 = LabelFrame(checklist) #Implementation frame
frame_3.grid(row=2,column=5,columnspan=2,pady=10)

#LABELS
"""Awardeded Study frame labels"""
awarded_study = Label(frame_1,text='Awarded Study')
internal_kom =Label(frame_1,text='Internal KOM')
check_wf = Label(frame_1, text="Check WF")
sls_task = Label(frame_1, text="Assign SLS in WF")
draft_lp = Label(frame_1, text="Draft loc. plan")

"""Localisation setup frame labels"""
loca_setup = Label(frame_2, text='Localisation setup')


"""Implementation frame"""
implementation = Label(frame_3, text="Implementation")
handover_ls = Label(frame_3, text="Handover LS")


#LABELS GRID
"""Awarded study frame"""
awarded_study.grid(row=0,column=0, columnspan=2, pady=10)
internal_kom.grid(row=1,column=0)
check_wf.grid(row=2,column=0)
sls_task.grid(row=3,column=0,)
draft_lp.grid(row=4,column=0)
"""Localisation setup frame"""
loca_setup.grid(row=0,column=0, columnspan=2,pady=10)


"""Implementation"""
implementation.grid(row=0,column=0, columnspan=2, pady=10)
handover_ls.grid(row=1,column=0)

#Variables for checkboxes
internal_kom_var=IntVar()
check_wf_var = IntVar()
sls_task_var = IntVar()
draft_lp_var = IntVar()

#CHECKBOXES
"""Awardeded Study frame checkboxex"""
internal_kom = Checkbutton(frame_1, variable=internal_kom_var)
check_wf = Checkbutton(frame_1, variable=check_wf_var)
sls_task = Checkbutton(frame_1, variable=sls_task_var)
draft_lp = Checkbutton(frame_1, variable=draft_lp_var)


#CHECKBOXES GRID
internal_kom.grid(row=1,column=1)
check_wf.grid(row=2,column=1,)
sls_task.grid(row=3,column=1)
draft_lp.grid(row=4,column=1)




checklist.mainloop()