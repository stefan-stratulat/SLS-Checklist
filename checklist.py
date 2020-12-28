from tkinter import *
from PIL import ImageTk, Image

"""Checklist main template, used to test the GUI before adding it into main"""

checklist = Tk()
checklist.title("SLS Checklist")
checklist.iconbitmap('images/fire_eye_alien.ico')
checklist.configure(bg="#add8e6")
checklist.geometry('1200x650')

#Checklist FRAMES
frame_0 = LabelFrame(checklist,bg="#2F4F4F") #Study info frame
frame_1 = LabelFrame(checklist) #Awarded study frame
frame_2 = LabelFrame(checklist) #Localisation setup frame
frame_3 = LabelFrame(checklist) #Implementation frame
frame_4 = LabelFrame(checklist)  #TO DO Frame

#function for the submit button

#Add Study
add_study = Button(checklist, text="Add study",padx=5,pady=5)
#Update study
update_study = Button(checklist, text="Update study info",padx=5,pady=5)
#MAIN GRID
frame_0.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=10,ipady=5)
frame_1.grid(row=0,column=2,columnspan=2,padx=10,pady=10)
frame_2.grid(row=0,column=4,columnspan=3,padx=10,pady=10,ipadx=10,ipady=5)
frame_3.grid(row=2,column=0,columnspan=3,padx=20,pady=10)
frame_4.grid(row=2,column=4,columnspan=4,padx=10,pady=10)
add_study.grid(row=3,column=0)
update_study.grid(row=3,column=2)


#Study info frame
sponsor = Label(frame_0, text="Sponsor")
sponsor.grid(row=0,column=0,pady=(10,0))
study_code = Label(frame_0, text="Study Code")
study_code.grid(row=1,column=0,pady=(10,0))
sponsor_box = Entry(frame_0,width=20)
sponsor_box.grid(row=0,column=1, pady=(10,0))
study_code_box = Entry(frame_0,width=20)
study_code_box.grid(row=1,column=1,pady=(10,0))
language_number = Label(frame_0, text="Language number")
language_number.grid(row=2,column=0,pady=(10,0))
language_number_box = Entry(frame_0,width=20)
language_number_box.grid(row=2,column=1,pady=(10,0))
pm_name = Label(frame_0, text="Project Manager")
pm_name.grid(row=3,column=0,pady=(10,0))
pm_name_box = Entry(frame_0, width=20)
pm_name_box.grid(row=3,column=1, pady=(10,0))
pds_name = Label(frame_0, text="Project Delivery Specialist")
pds_name.grid(row=4,column=0,pady=(10,0))
pds_name_box = Entry(frame_0, width=20)
pds_name_box.grid(row=4,column=1, pady=(10,0))
device_type = Label(frame_0,text="Device")
device_type.grid(row=5,column=0,pady=(10,0))
device_type_box=Entry(frame_0,width=20)
device_type_box.grid(row=5,column=1,pady=(10,0))
cis_label = Label(frame_0,text="CIS")
cis_label.grid(row=6,column=0,pady=(10,0))
cis_box= Entry(frame_0,width=20)
cis_box.grid(row=6,column=1,pady=(10,0))
translation_vendor = Label(frame_0, text="Translation vendor")
translation_vendor_box = Entry(frame_0, width=20)
translation_vendor.grid(row=7,column=0,pady=(10,0))
translation_vendor_box.grid(row=7,column=1,pady=(10,0))

"""Awardeded Study frame"""
#LABELS
awarded_study = Label(frame_1,text='Awarded Study',font='Arial 9 bold')
internal_kom =Label(frame_1,text='Internal KOM')
check_wf = Label(frame_1, text="Check WF plan")
sls_task = Label(frame_1, text="Assign SLS in WF")
draft_lp = Label(frame_1, text="Draft loc. plan")

internal_kom_box = Entry(frame_1,width=10)
check_wf_box = Entry(frame_1,width=10)
sls_task_box = Entry(frame_1,width=10)
draft_lp_box = Entry(frame_1,width=10)

"""Grid for Awarded study frame - frame_1"""
awarded_study.grid(row=0,column=0, columnspan=2, pady=10)
internal_kom.grid(row=1,column=0)
check_wf.grid(row=2,column=0)
sls_task.grid(row=3,column=0,)
draft_lp.grid(row=4,column=0)
internal_kom_box.grid(row=1,column=1)
check_wf_box.grid(row=2,column=1,)
sls_task_box.grid(row=3,column=1)
draft_lp_box.grid(row=4,column=1)

"""Localisation setup frame"""

#labels
loca_setup = Label(frame_2, text='Localisation setup',font='Arial 9 bold')
loca_kom = Label(frame_2, text='Localisation KOM date')
check_msr = Label(frame_2,text='Check Master SR')
check_mqrg = Label(frame_2,text='Check Master QRG/SUM')
check_ldc = Label(frame_2, text='Check master LDC is done')
check_paper_source = Label(frame_2, text="Check paper sources")
check_translation_service = Label(frame_2,text="Confirm translation services")
check_tft = Label(frame_2, text="Check if TFT is split per services/forms")
check_irb = Label(frame_2, text="Confirm IRB")
check_quote = Label(frame_2, text="Create quotation requests")
check_po = Label(frame_2, text="Create PO")
add_quote_po_oct = Label(frame_2, text="Add quote and PO in OCT")
loca_plan = Label(frame_2, text="Create final localisation plan")
access_ts_tm = Label(frame_2, text="Get access in TS and TM")
assign_ls_wf = Label(frame_2,text="Assign LS in WF")
access_platform = Label(frame_2,text="Get access in vendor platform(if needed)")

#boxex for localisation setup
loca_kom_box = Entry(frame_2,width=10)
check_msr_box = Entry(frame_2,width=10)
check_mqrg_box = Entry(frame_2,width=10)
check_ldc_box = Entry(frame_2,width=10)
check_paper_source_box = Entry(frame_2,width=10)
check_translation_service_box = Entry(frame_2,width=10)
check_tft_box = Entry(frame_2,width=10)
check_irb_box = Entry(frame_2,width=10)
check_quote_box = Entry(frame_2,width=10)
check_po_box = Entry(frame_2,width=10)
add_quote_po_oct_box = Entry(frame_2,width=10)
loca_plan_box = Entry(frame_2,width=10)
access_ts_tm_box = Entry(frame_2,width=10)
assign_ls_wf_box = Entry(frame_2,width=10)
access_platform_box= Entry(frame_2,width=10)

#grid for localisation setup
loca_setup.grid(row=0,column=0, columnspan=3,padx=70,pady=10)
loca_kom.grid(row=2,column=0)
check_msr.grid(row=3,column=0)
check_mqrg.grid(row=4,column=0)
check_ldc.grid(row=5,column=0)
check_paper_source.grid(row=6,column=0)
check_translation_service.grid(row=7,column=0)
check_tft.grid(row=8,column=0)
check_irb.grid(row=2,column=2)
check_quote.grid(row=3,column=2)
check_po.grid(row=4,column=2)
add_quote_po_oct.grid(row=5,column=2)
loca_plan.grid(row=6,column=2)
access_ts_tm.grid(row=7,column=2)
assign_ls_wf.grid(row=8,column=2)
access_platform.grid(row=9,column=2)
loca_kom_box.grid(row=2,column=1)
check_msr_box.grid(row=3,column=1)
check_mqrg_box.grid(row=4,column=1)
check_ldc_box.grid(row=5,column=1)
check_paper_source_box.grid(row=6,column=1)
check_translation_service_box.grid(row=7,column=1)
check_tft_box.grid(row=8,column=1)
check_irb_box.grid(row=2,column=3)
check_quote_box.grid(row=3,column=3)
check_po_box.grid(row=4,column=3)
add_quote_po_oct_box.grid(row=5,column=3)
loca_plan_box.grid(row=6,column=3)
access_ts_tm_box.grid(row=7,column=3)
assign_ls_wf_box.grid(row=8,column=3)
access_platform_box.grid(row=9,column=3)

"""Implementation frame"""
implementation = Label(frame_3, text="Implementation",font='Arial 9 bold')
handover_ls = Label(frame_3, text="Handover info to LS")
notes = Label(frame_3, text="NOTES",font='Arial 9 bold')
notes_text= Text(frame_3, width=40,height=10)


handover_ls_box =Entry(frame_3,width=10)

#grid
implementation.grid(row=0,column=0, columnspan=2, pady=10)
handover_ls.grid(row=1,column=0)
handover_ls_box.grid(row=1,column=1)
notes.grid(row=2,column=0,columnspan=2)
notes_text.grid(row=3,column=0,columnspan=2,padx=10,pady=5)


#TO DO Frame

to_do = Label(frame_4,text="TO DO",font='Arial 10 bold')
to_do_textbox = Text(frame_4,width=30,height=14,bd=3)

#grid
to_do.grid(row=0,column=1)
to_do_textbox.grid(row=1,column=0,columnspan=3,padx=5,pady=5,ipadx=10,ipady=10)

checklist.mainloop()
