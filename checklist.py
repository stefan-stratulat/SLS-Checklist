from tkinter import *
#CHECKLIST FORM

checklist = Tk()
checklist.title("SLS Checklist")
checklist.geometry('600x600')

#Checklist FRAMES
frame_0 = LabelFrame(checklist) #Study info frame
frame_0.grid(row=0,column=1,columnspan=2,padx=10,pady=10,ipadx=10,ipady=5)
frame_1 = LabelFrame(checklist) #Awarded study frame
frame_1.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
frame_2 = LabelFrame(checklist) #Localisation setup frame
frame_2.grid(row=3,column=1,columnspan=2,padx=10,pady=10)
frame_3 = LabelFrame(checklist) #Implementation frame
frame_3.grid(row=2,column=1,columnspan=2,padx=20,pady=10)


#Study info
sponsor = Label(frame_0, text="Sponsor")
sponsor.grid(row=0,column=0,pady=(10,0))
study_code = Label(frame_0, text="Study Code")
study_code.grid(row=1,column=0,pady=(10,0))
sponsor_box = Entry(frame_0,width=20)
sponsor_box.grid(row=0,column=1, pady=(10,0))
study_code_box = Entry(frame_0,width=20)
study_code_box.grid(row=1,column=1,pady=(10,0))

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
loca_setup.grid(row=0,column=0, columnspan=3,padx=70,pady=10)
loca_kom.grid(row=2,column=0)
c_msr.grid(row=3,column=0)
c_mqrg.grid(row=4,column=0)
c_ldc.grid(row=5,column=0)
c_paper_source.grid(row=6,column=0)
c_translation_service.grid(row=7,column=0)
c_tft.grid(row=8,column=0)
c_irb.grid(row=2,column=2)
c_quote.grid(row=3,column=2)
c_po.grid(row=4,column=2)
quote_po_oct.grid(row=5,column=2)
loca_plan.grid(row=6,column=2)
access_ts_tm.grid(row=7,column=2)
assign_ls_wf.grid(row=8,column=2)


"""Implementation"""
implementation.grid(row=0,column=0, columnspan=2, pady=10)
handover_ls.grid(row=1,column=0)

#Variables for checkboxes
"""Awarded studies"""
internal_kom_var = IntVar()
check_wf_var = IntVar()
sls_task_var = IntVar()
draft_lp_var = IntVar()

"""Localisation setup var"""
loca_setup_var = IntVar()
loca_kom_var = IntVar()
c_msr_var = IntVar()
c_mqrg_var = IntVar()
c_ldc_var = IntVar()
c_paper_source_var = IntVar()
c_translation_service_var = IntVar()
c_tft_var = IntVar()
c_irb_var = IntVar()
c_quote_var = IntVar()
c_po_var = IntVar()
quote_po_oct_var = IntVar()
loca_plan_var = IntVar()
access_ts_tm_var = IntVar()
assign_ls_wf_var = IntVar()

#CHECKBOXES
"""Awardeded Study frame checkboxes"""
internal_kom_cb = Checkbutton(frame_1, variable=internal_kom_var)
check_wf_cb = Checkbutton(frame_1, variable=check_wf_var)
sls_task_cb = Checkbutton(frame_1, variable=sls_task_var)
draft_lp_cb = Checkbutton(frame_1, variable=draft_lp_var)

"""Localisation setup checkboxes"""
loca_kom_cb = Checkbutton(frame_2, variable=loca_kom_var)
c_msr_cb = Checkbutton(frame_2, variable=c_msr_var)
c_mqrg_cb = Checkbutton(frame_2, variable=c_mqrg_var)
c_ldc_cb = Checkbutton(frame_2, variable=c_ldc_var)
c_paper_source_cb = Checkbutton(frame_2, variable=c_paper_source_var)
c_translation_service_cb = Checkbutton(frame_2, variable=c_translation_service_var)
c_tft_cb = Checkbutton(frame_2, variable=c_tft_var)
c_irb_cb = Checkbutton(frame_2, variable=c_irb_var)
c_quote_cb = Checkbutton(frame_2, variable=c_quote_var)
c_po_cb = Checkbutton(frame_2, variable=c_po_var)
quote_po_oct_cb = Checkbutton(frame_2, variable=quote_po_oct_var)
loca_plan_cb = Checkbutton(frame_2, variable=loca_plan_var)
access_ts_tm_cb = Checkbutton(frame_2, variable=access_ts_tm_var)
assign_ls_wf_cb = Checkbutton(frame_2, variable=assign_ls_wf_var)

#CHECKBOXES GRID
"""Awarded study"""
internal_kom_cb.grid(row=1,column=1)
check_wf_cb.grid(row=2,column=1,)
sls_task_cb.grid(row=3,column=1)
draft_lp_cb.grid(row=4,column=1)

"""Localisation setup"""
loca_kom_cb.grid(row=2,column=1)
c_msr_cb.grid(row=3,column=1)
c_mqrg_cb.grid(row=4,column=1)
c_ldc_cb.grid(row=5,column=1)
c_paper_source_cb.grid(row=6,column=1)
c_translation_service_cb.grid(row=7,column=1)
c_tft_cb.grid(row=8,column=1)
c_irb_cb.grid(row=2,column=3)
c_quote_cb.grid(row=3,column=3)
c_po_cb.grid(row=4,column=3)
quote_po_oct_cb.grid(row=5,column=3)
loca_plan_cb.grid(row=6,column=3)
access_ts_tm_cb.grid(row=7,column=3)
assign_ls_wf_cb.grid(row=8,column=3)


checklist.mainloop()