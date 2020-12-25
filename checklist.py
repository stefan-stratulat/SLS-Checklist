from tkinter import *
#CHECKLIST FORM

def checklist():
    checklist = Tk()
    checklist.title("SLS Checklist")
    checklist.geometry('1080x600')

    #Checklist FRAMES
    frame_0 = LabelFrame(checklist) #Study info frame
    frame_0.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=10,ipady=5)
    frame_1 = LabelFrame(checklist) #Awarded study frame
    frame_1.grid(row=0,column=2,columnspan=2,padx=10,pady=10)
    frame_2 = LabelFrame(checklist) #Localisation setup frame
    frame_2.grid(row=0,column=4,columnspan=3,padx=10,pady=10,ipadx=10,ipady=5)
    frame_3 = LabelFrame(checklist) #Implementation frame
    frame_3.grid(row=2,column=0,columnspan=3,padx=20,pady=10)
    frame_4 = LabelFrame(checklist)  #TO DO Frame
    frame_4.grid(row=2,column=4,columnspan=4,padx=10,pady=10)


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
    ps_name = Label(frame_0, text="Project Delivery Specialist")
    ps_name.grid(row=4,column=0,pady=(10,0))
    ps_name_box = Entry(frame_0, width=20)
    ps_name_box.grid(row=4,column=1, pady=(10,0))
    device_type = Label(frame_0,text="Device")
    device_type.grid(row=5,column=0,pady=(10,0))
    device_type_box=Entry(frame_0,width=20)
    device_type_box.grid(row=5,column=1,pady=(10,0))


    """Awardeded Study frame"""
    #LABELS
    awarded_study = Label(frame_1,text='Awarded Study')
    internal_kom =Label(frame_1,text='Internal KOM')
    check_wf = Label(frame_1, text="Check WF plan")
    sls_task = Label(frame_1, text="Assign SLS in WF")
    draft_lp = Label(frame_1, text="Draft loc. plan")

    #variables for checkboxex
    internal_kom_var = IntVar()
    check_wf_var = IntVar()
    sls_task_var = IntVar()
    draft_lp_var = IntVar()

    #CHECKBOXES
    """Awardeded Study frame checkboxes"""
    internal_kom_cb = Checkbutton(frame_1, variable=internal_kom_var)
    check_wf_cb = Checkbutton(frame_1, variable=check_wf_var)
    sls_task_cb = Checkbutton(frame_1, variable=sls_task_var)
    draft_lp_cb = Checkbutton(frame_1, variable=draft_lp_var)

    #grid
    awarded_study.grid(row=0,column=0, columnspan=2, pady=10)
    internal_kom.grid(row=1,column=0)
    check_wf.grid(row=2,column=0)
    sls_task.grid(row=3,column=0,)
    draft_lp.grid(row=4,column=0)
    internal_kom_cb.grid(row=1,column=1)
    check_wf_cb.grid(row=2,column=1,)
    sls_task_cb.grid(row=3,column=1)
    draft_lp_cb.grid(row=4,column=1)

    """Localisation setup frame"""

    #labels
    loca_setup = Label(frame_2, text='Localisation setup')
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
    quote_po_oct = Label(frame_2, text="Add quote and PO in OCT")
    loca_plan = Label(frame_2, text="Create final localisation plan")
    access_ts_tm = Label(frame_2, text="Get access in TS and TM")
    assign_ls_wf = Label(frame_2,text="Assing LS in WF")
    access_plaform = Label(frame_2,text="Get access in vendor platform(if needed)")

    #variables for localisation setup frame checkboxes
    loca_setup_var = IntVar()
    loca_kom_var = IntVar()
    check_msr_var = IntVar()
    check_mqrg_var = IntVar()
    check_ldc_var = IntVar()
    check_paper_source_var = IntVar()
    check_translation_service_var = IntVar()
    check_tft_var = IntVar()
    check_irb_var = IntVar()
    check_quote_var = IntVar()
    check_po_var = IntVar()
    quote_po_oct_var = IntVar()
    loca_plan_var = IntVar()
    access_ts_tm_var = IntVar()
    assign_ls_wf_var = IntVar()
    access_plaform_var = IntVar()

    #checkboxes for localisation setup
    loca_kom_cb = Checkbutton(frame_2, variable=loca_kom_var)
    check_msr_cb = Checkbutton(frame_2, variable=check_msr_var)
    check_mqrg_cb = Checkbutton(frame_2, variable=check_mqrg_var)
    check_ldc_cb = Checkbutton(frame_2, variable=check_ldc_var)
    check_paper_source_cb = Checkbutton(frame_2, variable=check_paper_source_var)
    check_translation_service_cb = Checkbutton(frame_2, variable=check_translation_service_var)
    check_tft_cb = Checkbutton(frame_2, variable=check_tft_var)
    check_irb_cb = Checkbutton(frame_2, variable=check_irb_var)
    check_quote_cb = Checkbutton(frame_2, variable=check_quote_var)
    check_po_cb = Checkbutton(frame_2, variable=check_po_var)
    quote_po_oct_cb = Checkbutton(frame_2, variable=quote_po_oct_var)
    loca_plan_cb = Checkbutton(frame_2, variable=loca_plan_var)
    access_ts_tm_cb = Checkbutton(frame_2, variable=access_ts_tm_var)
    assign_ls_wf_cb = Checkbutton(frame_2, variable=assign_ls_wf_var)
    access_plaform_cb=Checkbutton(frame_2, variable=access_plaform_var)

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
    quote_po_oct.grid(row=5,column=2)
    loca_plan.grid(row=6,column=2)
    access_ts_tm.grid(row=7,column=2)
    assign_ls_wf.grid(row=8,column=2)
    access_plaform.grid(row=9,column=2)
    loca_kom_cb.grid(row=2,column=1)
    check_msr_cb.grid(row=3,column=1)
    check_mqrg_cb.grid(row=4,column=1)
    check_ldc_cb.grid(row=5,column=1)
    check_paper_source_cb.grid(row=6,column=1)
    check_translation_service_cb.grid(row=7,column=1)
    check_tft_cb.grid(row=8,column=1)
    check_irb_cb.grid(row=2,column=3)
    check_quote_cb.grid(row=3,column=3)
    check_po_cb.grid(row=4,column=3)
    quote_po_oct_cb.grid(row=5,column=3)
    loca_plan_cb.grid(row=6,column=3)
    access_ts_tm_cb.grid(row=7,column=3)
    assign_ls_wf_cb.grid(row=8,column=3)
    access_plaform_cb.grid(row=9,column=3)

    """Implementation frame"""
    implementation = Label(frame_3, text="Implementation")
    handover_ls = Label(frame_3, text="Handover info to LS")
    notes = Label(frame_3, text="NOTES")
    notes_text= Text(frame_3, width=40,height=10)

    handover_ls_var=IntVar()
    handover_ls_cb =Checkbutton(frame_3, variable=handover_ls_var)

    #grid
    implementation.grid(row=0,column=0, columnspan=2, pady=10)
    handover_ls.grid(row=1,column=0)
    handover_ls_cb.grid(row=1,column=1)
    notes.grid(row=2,column=0,columnspan=2)
    notes_text.grid(row=3,column=0,columnspan=2,padx=10,pady=5)


    #TO DO Frame

    to_do = Label(frame_4,text="TO DO")
    to_do_textbox = Text(frame_4,width=35,height=15)

    #grid
    to_do.grid(row=0,column=0,columnspan=3)
    to_do_textbox.grid(row=1,column=0,columnspan=4)



    checklist.mainloop()