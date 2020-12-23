from tkinter import *
#CHECKLIST FORM

checklist = Tk()
checklist.title("SLS Checklist")
checklist.geometry('600x600')


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
frame_1.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
frame_2 = LabelFrame(checklist) #Localisation setup frame
frame_2.grid(row=2,column=3,columnspan=2,pady=10)
frame_3 = LabelFrame(checklist) #Implementation frame
frame_3.grid(row=2,column=5,columnspan=2,padx=10,pady=10)

#LABELS
"""Awardeded Study frame labels"""
awarded_study = Label(frame_1,text='Awarded Study')
internal_kom =Label(frame_1,text='Internal KOM')
check_wf = Label(frame_1, text="Check WF")
sls_task = Label(frame_1, text="Assign SLS in WF")
draft_lp = Label(frame_1, text="Draft loc. plan")

"""Localisation setup frame labels"""
loca_setup = Label(frame_2, text='Localisation setup')
loca_kom = Label(frame_2, text='Localisation KOM date')
c_msr = Label(frame_2,text='Check Master SR')
c_mqrg = Label(frame_2,text='Check Master QRG')
c_ldc = Label(frame_2, text='Check master LDC is done')
c_paper_source = Label(frame_2, text="Check paper sources")
c_translation_service = Label(frame_2,text="Confirm translation services")
c_tft = Label(frame_2, text="Check if TFT is split per services/forms")
c_irb = Label(frame_2, text="Confirm IRB")
c_quote = Label(frame_2, text="Create quotation requests")
c_po = Label(frame_2, text="Create PO")
quote_po_oct = Label(frame_2, text="Add quote and PO in OCT")
loca_plan = Label(frame_2, text="Create final localisation plan")
access_ts_tm = Label(frame_2, text="Get access in TS and TM")
assign_ls_wf = Label(frame_2,text="Assing LS in WF")

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

"""Implementation"""
loca_setup.grid(row=1,column=0)
loca_kom.grid(row=2,column=0)
c_msr.grid(row=3,column=0)
c_mqrg.grid(row=4,column=0)
c_ldc.grid(row=5,column=0)
c_paper_source.grid(row=6,column=0)
c_translation_service.grid(row=7,column=0)
c_tft.grid(row=8,column=0)
c_irb.grid(row=9,column=0)
c_quote.grid(row=10,column=0)
c_po.grid(row=11,column=0)
quote_po_oct.grid(row=12,column=0)
loca_plan.grid(row=13,column=0)
access_ts_tm.grid(row=14,column=0)
assign_ls_wf.grid(row=15,column=0)


#CHECKBOXES GRID
internal_kom.grid(row=1,column=1)
check_wf.grid(row=2,column=1,)
sls_task.grid(row=3,column=1)
draft_lp.grid(row=4,column=1)




checklist.mainloop()