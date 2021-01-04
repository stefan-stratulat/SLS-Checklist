from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
import os


root = Tk()
root.title("SLS Checklist")
root.iconbitmap('images/fire_eye_alien.ico')
root.configure(bg="#add8e6")
root.geometry('500x300')

"""Function to show the initial SLS checklist to add study"""
def frames():
    checklist = Tk()
    checklist.title("SLS Checklist")
    checklist.iconbitmap('images/fire_eye_alien.ico')
    checklist.configure(bg="#add8e6")
    checklist.geometry('1200x650')

    #Checklist FRAMES
    frame_0 = LabelFrame(checklist) #Study info frame
    frame_1 = LabelFrame(checklist) #Awarded study frame
    frame_2 = LabelFrame(checklist) #Localisation setup frame
    frame_3 = LabelFrame(checklist) #Implementation frame
    frame_4 = LabelFrame(checklist)  #TO DO Frame

    #function for the submit button
    def submit():
        conn = sqlite3.connect('studies.db')
        c =  conn.cursor()
        c.execute('''INSERT INTO studies VALUES(
                :sponsor,
                :study_code,
                :language_number,
                :pm_name,
                :pds_name,
                :device_type,
                :translation_vendor,
                :cis,
                :internal_kom,
                :check_wf,
                :sls_task,
                :draft_lp,
                :loca_kom,
                :check_msr,
                :check_mqrg,
                :check_ldc,
                :check_paper_source,
                :check_translation_service,
                :check_tft,
                :check_irb,
                :check_quote,
                :check_po,
                :add_quote_po_oct,
                :loca_plan,
                :access_ts_tm,
                :assign_ls_wf,
                :access_platform,
                :handover_ls,
                :notes,
                :to_do)''',
                {"sponsor": sponsor_box.get(),
                "study_code": study_code_box.get(),
                "language_number": language_number_box.get(),
                "pm_name": pm_name_box.get(),
                "pds_name": pds_name_box.get(),
                "device_type": device_type_box.get(),
                "translation_vendor": translation_vendor_box.get(),
                "cis": cis_box.get(),
                "internal_kom": internal_kom_box.get(),
                "check_wf": check_wf_box.get(),
                "sls_task": sls_task_box.get(),
                "draft_lp": draft_lp_box.get(),
                "loca_kom": loca_kom_box.get(),
                "check_msr": check_msr_box.get(),
                "check_mqrg": check_mqrg_box.get(),
                "check_ldc": check_ldc_box.get(),
                "check_paper_source": check_paper_source_box.get(),
                "check_translation_service": check_translation_service_box.get(),
                "check_tft": check_tft_box.get(),
                "check_irb": check_irb_box.get(),
                "check_quote": check_quote_box.get(),
                "check_po": check_po_box.get(),
                "add_quote_po_oct": add_quote_po_oct_box.get(),
                "loca_plan": loca_plan_box.get(),
                "access_ts_tm": access_ts_tm_box.get(),
                "assign_ls_wf": assign_ls_wf_box.get(),
                "access_platform": access_platform_box.get(),
                "handover_ls": handover_ls_box.get(),
                "notes": notes_text.get(1.0,END),
                "to_do": to_do_textbox.get(1.0,END)
                })
        conn.commit()
        conn.close()
        checklist.destroy()

    #Add Study
    add_study = Button(checklist, text="Add study",command=submit, padx=5,pady=5)

    #MAIN GRID
    frame_0.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=10,ipady=5)
    frame_1.grid(row=0,column=2,columnspan=2,padx=10,pady=10)
    frame_2.grid(row=0,column=4,columnspan=3,padx=10,pady=10,ipadx=10,ipady=5)
    frame_3.grid(row=2,column=0,columnspan=3,padx=20,pady=10)
    frame_4.grid(row=2,column=4,columnspan=4,padx=10,pady=10)
    add_study.grid(row=3,column=0)


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
    translation_vendor = Label(frame_0, text="Translation vendor")
    translation_vendor_box = Entry(frame_0, width=20)
    translation_vendor.grid(row=6,column=0,pady=(10,0))
    translation_vendor_box.grid(row=6,column=1,pady=(10,0))
    cis_label = Label(frame_0,text="CIS")
    cis_label.grid(row=7,column=0,pady=(10,0))
    cis_box= Entry(frame_0,width=20)
    cis_box.grid(row=7,column=1,pady=(10,0))

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

"""function for showing the data in the database"""
def show():
    """Function that will show all the studies in the DB by study code and record ID"""
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()

    #Query the database
    c.execute("SELECT oid,* FROM studies")
    records = c.fetchall()

    print_records = "ID"+"  "+"Study Code"+"\n"
    for record in records:
        print_records += str(record[0])+ " "+str(record[2]) +"\n"

    query_label = Label(root, text=print_records,bg="#add8e6")
    query_label.grid(row=1, column=3, columnspan=2,rowspan=30,sticky=N)

    conn.commit()
    conn.close()

#function to edit and update the data in the database
def editor():
    """Edited frames with DB data, e stands for editor"""
    e_checklist = Tk()
    e_checklist.title("Update SLS Checklist")
    e_checklist.iconbitmap('images/fire_eye_alien.ico')
    e_checklist.configure(bg="#add8e6")
    e_checklist.geometry('1200x650')

    """Function for the handover LS button, gather data from Awarded study frame"""
    def handover_ls_report():
        conn = sqlite3.connect('studies.db')
        c = conn.cursor()
        conn = sqlite3.connect('studies.db')
        c = conn.cursor()

        handover_ls_file = open('handover_ls.txt','w+')
        """data that will be writen on the txt file"""
        handover_ls_file.write('Sponsor: '+ e_sponsor_box.get()+'\n')
        handover_ls_file.write('Study code: '+ e_study_code_box.get()+'\n')
        handover_ls_file.write('Language number: '+ e_language_number_box.get()+'\n')
        handover_ls_file.write('PM: '+ e_pm_name_box.get()+'\n')
        handover_ls_file.write('PDS: '+ e_pds_name_box.get()+'\n')
        handover_ls_file.write('Device: '+ e_device_type_box.get()+'\n')
        handover_ls_file.write('Translation vendor: '+ e_translation_vendor_box.get()+'\n')
        handover_ls_file.write('CIS: '+ e_cis_box.get())
        handover_ls_file.close()
        """open the file in windows after it's written and closed by python"""
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        file_path = absolute_path + '\handover_ls.txt'
        os.startfile(file_path)

    #Checklist FRAMES
    e_frame_0 = LabelFrame(e_checklist) #Study info frame
    e_frame_1 = LabelFrame(e_checklist) #Awarded study frame
    e_frame_2 = LabelFrame(e_checklist) #Localisation setup frame
    e_frame_3 = LabelFrame(e_checklist) #Implementation frame
    e_frame_4 = LabelFrame(e_checklist)  #TO DO Frame

    #global variables
    global e_sponsor_box
    global e_study_code_box
    global e_language_number_box
    global e_pm_name_box
    global e_pds_name_box
    global e_device_type_box
    global e_translation_vendor_box
    global e_cis_box
    global e_internal_kom_box
    global e_check_wf_box
    global e_sls_task_box
    global e_draft_lp_box
    global e_loca_kom_box
    global e_check_msr_box
    global e_check_mqrg_box
    global e_check_ldc_box
    global e_check_paper_source_box
    global e_check_translation_service_box
    global e_check_tft_box
    global e_check_irb_box
    global e_check_quote_box
    global e_check_po_box
    global e_add_quote_po_oct_box
    global e_loca_plan_box
    global e_access_ts_tm_box
    global e_assign_ls_wf_box
    global e_access_platform_box
    global e_handover_ls_box
    global e_notes_text
    global e_to_do_textbox


    #Update study
    e_update_study_btn = Button(e_checklist, text="Update study info",command=update_info,padx=5,pady=5)

    handover_ls_report_btn = Button(e_checklist, text="Handover LS", command=handover_ls_report,padx=5,pady=5)
    #MAIN GRID
    e_frame_0.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=10,ipady=5)
    e_frame_1.grid(row=0,column=2,columnspan=2,padx=10,pady=10)
    e_frame_2.grid(row=0,column=4,columnspan=3,padx=10,pady=10,ipadx=10,ipady=5)
    e_frame_3.grid(row=2,column=0,columnspan=3,padx=20,pady=10)
    e_frame_4.grid(row=2,column=4,columnspan=4,padx=10,pady=10)
    e_update_study_btn.grid(row=3,column=0)
    handover_ls_report_btn.grid(row=3,column=2)


    #Study info frame
    e_sponsor = Label(e_frame_0, text="Sponsor")
    e_sponsor.grid(row=0,column=0,pady=(10,0))
    e_study_code = Label(e_frame_0, text="Study Code")
    e_study_code.grid(row=1,column=0,pady=(10,0))
    e_sponsor_box = Entry(e_frame_0,width=20)
    e_sponsor_box.grid(row=0,column=1, pady=(10,0))
    e_study_code_box = Entry(e_frame_0,width=20)
    e_study_code_box.grid(row=1,column=1,pady=(10,0))
    e_language_number = Label(e_frame_0, text="Language number")
    e_language_number.grid(row=2,column=0,pady=(10,0))
    e_language_number_box = Entry(e_frame_0,width=20)
    e_language_number_box.grid(row=2,column=1,pady=(10,0))
    e_pm_name = Label(e_frame_0, text="Project Manager")
    e_pm_name.grid(row=3,column=0,pady=(10,0))
    e_pm_name_box = Entry(e_frame_0, width=20)
    e_pm_name_box.grid(row=3,column=1, pady=(10,0))
    e_pds_name = Label(e_frame_0, text="Project Delivery Specialist")
    e_pds_name.grid(row=4,column=0,pady=(10,0))
    e_pds_name_box = Entry(e_frame_0, width=20)
    e_pds_name_box.grid(row=4,column=1, pady=(10,0))
    e_device_type = Label(e_frame_0,text="Device")
    e_device_type.grid(row=5,column=0,pady=(10,0))
    e_device_type_box=Entry(e_frame_0,width=20)
    e_device_type_box.grid(row=5,column=1,pady=(10,0))
    e_translation_vendor = Label(e_frame_0, text="Translation vendor")
    e_translation_vendor_box = Entry(e_frame_0, width=20)
    e_translation_vendor.grid(row=6,column=0,pady=(10,0))
    e_translation_vendor_box.grid(row=6,column=1,pady=(10,0))
    e_cis_label = Label(e_frame_0,text="CIS")
    e_cis_label.grid(row=7,column=0,pady=(10,0))
    e_cis_box= Entry(e_frame_0,width=20)
    e_cis_box.grid(row=7,column=1,pady=(10,0))


    """Awardeded Study frame"""
    #LABELS
    e_awarded_study = Label(e_frame_1,text='Awarded Study',font='Arial 9 bold')
    e_internal_kom =Label(e_frame_1,text='Internal KOM')
    e_check_wf = Label(e_frame_1, text="Check WF plan")
    e_sls_task = Label(e_frame_1, text="Assign SLS in WF")
    e_draft_lp = Label(e_frame_1, text="Draft loc. plan")


    e_internal_kom_box = Entry(e_frame_1,width=10)
    e_check_wf_box = Entry(e_frame_1,width=10)
    e_sls_task_box = Entry(e_frame_1,width=10)
    e_draft_lp_box = Entry(e_frame_1,width=10)

    #grid
    e_awarded_study.grid(row=0,column=0, columnspan=2, pady=10)
    e_internal_kom.grid(row=1,column=0)
    e_check_wf.grid(row=2,column=0)
    e_sls_task.grid(row=3,column=0,)
    e_draft_lp.grid(row=4,column=0)
    e_internal_kom_box.grid(row=1,column=1)
    e_check_wf_box.grid(row=2,column=1,)
    e_sls_task_box.grid(row=3,column=1)
    e_draft_lp_box.grid(row=4,column=1)

    """Localisation setup frame"""

    #labels
    e_loca_setup = Label(e_frame_2, text='Localisation setup',font='Arial 9 bold')
    e_loca_kom = Label(e_frame_2, text='Localisation KOM date')
    e_check_msr = Label(e_frame_2,text='Check Master SR')
    e_check_mqrg = Label(e_frame_2,text='Check Master QRG/SUM')
    e_check_ldc = Label(e_frame_2, text='Check master LDC is done')
    e_check_paper_source = Label(e_frame_2, text="Check paper sources")
    e_check_translation_service = Label(e_frame_2,text="Confirm translation services")
    e_check_tft = Label(e_frame_2, text="Check if TFT is split per services/forms")
    e_check_irb = Label(e_frame_2, text="Confirm IRB")
    e_check_quote = Label(e_frame_2, text="Create quotation requests")
    e_check_po = Label(e_frame_2, text="Create PO")
    e_add_quote_po_oct = Label(e_frame_2, text="Add quote and PO in OCT")
    e_loca_plan = Label(e_frame_2, text="Create final localisation plan")
    e_access_ts_tm = Label(e_frame_2, text="Get access in TS and TM")
    e_assign_ls_wf = Label(e_frame_2,text="Assign LS in WF")
    e_access_platform = Label(e_frame_2,text="Get access in vendor platform(if needed)")


    #checkboxes for localisation setup
    e_loca_kom_box = Entry(e_frame_2,width=10)
    e_check_msr_box = Entry(e_frame_2,width=10)
    e_check_mqrg_box = Entry(e_frame_2,width=10)
    e_check_ldc_box = Entry(e_frame_2,width=10)
    e_check_paper_source_box = Entry(e_frame_2,width=10)
    e_check_translation_service_box = Entry(e_frame_2,width=10)
    e_check_tft_box = Entry(e_frame_2,width=10)
    e_check_irb_box = Entry(e_frame_2,width=10)
    e_check_quote_box = Entry(e_frame_2,width=10)
    e_check_po_box = Entry(e_frame_2,width=10)
    e_add_quote_po_oct_box = Entry(e_frame_2,width=10)
    e_loca_plan_box = Entry(e_frame_2,width=10)
    e_access_ts_tm_box = Entry(e_frame_2,width=10)
    e_assign_ls_wf_box = Entry(e_frame_2,width=10)
    e_access_platform_box= Entry(e_frame_2,width=10)

    #grid for localisation setup
    e_loca_setup.grid(row=0,column=0, columnspan=3,padx=70,pady=10)
    e_loca_kom.grid(row=2,column=0)
    e_check_msr.grid(row=3,column=0)
    e_check_mqrg.grid(row=4,column=0)
    e_check_ldc.grid(row=5,column=0)
    e_check_paper_source.grid(row=6,column=0)
    e_check_translation_service.grid(row=7,column=0)
    e_check_tft.grid(row=8,column=0)
    e_check_irb.grid(row=2,column=2)
    e_check_quote.grid(row=3,column=2)
    e_check_po.grid(row=4,column=2)
    e_add_quote_po_oct.grid(row=5,column=2)
    e_loca_plan.grid(row=6,column=2)
    e_access_ts_tm.grid(row=7,column=2)
    e_assign_ls_wf.grid(row=8,column=2)
    e_access_platform.grid(row=9,column=2)
    e_loca_kom_box.grid(row=2,column=1)
    e_check_msr_box.grid(row=3,column=1)
    e_check_mqrg_box.grid(row=4,column=1)
    e_check_ldc_box.grid(row=5,column=1)
    e_check_paper_source_box.grid(row=6,column=1)
    e_check_translation_service_box.grid(row=7,column=1)
    e_check_tft_box.grid(row=8,column=1)
    e_check_irb_box.grid(row=2,column=3)
    e_check_quote_box.grid(row=3,column=3)
    e_check_po_box.grid(row=4,column=3)
    e_add_quote_po_oct_box.grid(row=5,column=3)
    e_loca_plan_box.grid(row=6,column=3)
    e_access_ts_tm_box.grid(row=7,column=3)
    e_assign_ls_wf_box.grid(row=8,column=3)
    e_access_platform_box.grid(row=9,column=3)

    """Implementation frame"""
    e_implementation = Label(e_frame_3, text="Implementation",font='Arial 9 bold')
    e_handover_ls = Label(e_frame_3, text="Handover info to LS")
    e_notes = Label(e_frame_3, text="NOTES",font='Arial 9 bold')
    e_notes_text= Text(e_frame_3, width=40,height=10)

    e_handover_ls_box = Entry(e_frame_3, width=10)

    #grid
    e_implementation.grid(row=0,column=0, columnspan=2, pady=10)
    e_handover_ls.grid(row=1,column=0)
    e_handover_ls_box.grid(row=1,column=1)
    e_notes.grid(row=2,column=0,columnspan=2)
    e_notes_text.grid(row=3,column=0,columnspan=2,padx=10,pady=5)


    #TO DO Frame

    e_to_do = Label(e_frame_4,text="TO DO",font='Arial 10 bold')
    e_to_do_textbox = Text(e_frame_4,width=30,height=14,bd=3)

    #grid
    e_to_do.grid(row=0,column=1)
    e_to_do_textbox.grid(row=1,column=0,columnspan=3,padx=5,pady=5,ipadx=10,ipady=10)



    #coonect to the database
    conn = sqlite3.connect('studies.db')
    c =  conn.cursor()

    #querry the DB based on the ID of the study
    record_id = search_box.get()
    c.execute("SELECT * FROM studies WHERE oid = " + record_id)
    records=c.fetchall()

    #loop to add all the existing data in the
    for record in records:
        e_sponsor_box.insert(0, record[0])
        e_study_code_box.insert(0, record[1])
        e_language_number_box.insert(0, record[2])
        e_pm_name_box.insert(0, record[3])
        e_pds_name_box.insert(0, record[4])
        e_device_type_box.insert(0, record[5])
        e_translation_vendor_box.insert(0,record[6])
        e_cis_box.insert(0,record[7])
        e_internal_kom_box.insert(0, record[8])
        e_check_wf_box.insert(0, record[9])
        e_sls_task_box.insert(0, record[10])
        e_draft_lp_box.insert(0, record[11])
        e_loca_kom_box.insert(0, record[12])
        e_check_msr_box.insert(0, record[13])
        e_check_mqrg_box.insert(0, record[14])
        e_check_ldc_box.insert(0, record[15])
        e_check_paper_source_box.insert(0, record[16])
        e_check_translation_service_box.insert(0, record[17])
        e_check_tft_box.insert(0, record[18])
        e_check_irb_box.insert(0, record[19])
        e_check_quote_box.insert(0, record[20])
        e_check_po_box.insert(0, record[21])
        e_add_quote_po_oct_box.insert(0, record[22])
        e_loca_plan_box.insert(0, record[23])
        e_access_ts_tm_box.insert(0, record[24])
        e_assign_ls_wf_box.insert(0, record[25])
        e_access_platform_box.insert(0, record[26])
        e_handover_ls_box.insert(0, record[27])
        e_notes_text.insert(1.0, record[28])
        e_to_do_textbox.insert(1.0, record[29])


    conn.commit()
    conn.close()
    e_checklist.mainloop()

"""function for Update study info in the editor function"""
def update_info():
    conn = sqlite3.connect("studies.db")
    c =conn.cursor()

    record_id = search_box.get()
    c.execute("""UPDATE studies SET
        sponsor = :sponsor,
        study_code = :study_code,
        language_number = :language_number,
        pm_name = :pm_name,
        pds_name = :pds_name,
        device_type = :device_type,
        translation_vendor = :translation_vendor,
        cis = :cis,
        internal_kom = :internal_kom,
        check_wf = :check_wf,
        sls_task = :sls_task,
        draft_lp = :draft_lp,
        loca_kom = :loca_kom,
        check_msr = :check_msr,
        check_mqrg = :check_mqrg,
        check_ldc = :check_ldc,
        check_paper_source = :check_paper_source,
        check_translation_service = :check_translation_service,
        check_tft = :check_tft,
        check_irb = :check_irb,
        check_quote = :check_quote,
        check_po = :check_po,
        add_quote_po_oct = :add_quote_po_oct,
        loca_plan = :loca_plan,
        access_ts_tm = :access_ts_tm,
        assign_ls_wf = :assign_ls_wf,
        access_platform = :access_platform,
        handover_ls = :handover_ls,
        notes = :notes,
        to_do = :to_do
        WHERE oid = :oid""",
        {"sponsor": e_sponsor_box.get(),
        "study_code": e_study_code_box.get(),
        "language_number": e_language_number_box.get(),
        "pm_name": e_pm_name_box.get(),
        "pds_name": e_pds_name_box.get(),
        "device_type": e_device_type_box.get(),
        "translation_vendor": e_translation_vendor_box.get(),
        "cis": e_cis_box.get(),
        "internal_kom": e_internal_kom_box.get(),
        "check_wf": e_check_wf_box.get(),
        "sls_task": e_sls_task_box.get(),
        "draft_lp": e_draft_lp_box.get(),
        "loca_kom": e_loca_kom_box.get(),
        "check_msr": e_check_msr_box.get(),
        "check_mqrg": e_check_mqrg_box.get(),
        "check_ldc": e_check_ldc_box.get(),
        "check_paper_source": e_check_paper_source_box.get(),
        "check_translation_service": e_check_translation_service_box.get(),
        "check_tft": e_check_tft_box.get(),
        "check_irb": e_check_irb_box.get(),
        "check_quote": e_check_quote_box.get(),
        "check_po": e_check_po_box.get(),
        "add_quote_po_oct": e_add_quote_po_oct_box.get(),
        "loca_plan": e_loca_plan_box.get(),
        "access_ts_tm": e_access_ts_tm_box.get(),
        "assign_ls_wf": e_assign_ls_wf_box.get(),
        "access_platform": e_access_platform_box.get(),
        "handover_ls": e_handover_ls_box.get(),
        "notes": e_notes_text.get(1.0,END),
        "to_do": e_to_do_textbox.get(1.0,END),
        'oid': record_id})

    conn.commit()
    conn.close()

"""function to delete a study"""
def delete():
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()
    record_id = search_box.get()
    #Query the database for study code
    c.execute("SELECT study_code FROM studies WHERE oid= "+record_id)
    queried_study = c.fetchone()
    #ask user to confirm the study code they want to delete
    message = messagebox.askquestion(title="Delete",message=f"Are you sure you want to delete record {record_id}, study code{queried_study}?")
    if message =='yes':
        #delete the record from DB after user press yes
        c.execute("DELETE from studies WHERE oid= "+record_id)
    else:
        return

    conn.commit()
    conn.close()
    #clear the search box
    search_box.delete(0, END)

"""function to show a new window with all to do tasks"""
def to_do_report():
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()

    """create a new window that will show the report"""

    c.execute("SELECT study_code,to_do FROM studies")
    records = c.fetchall()

    to_do_file = open('to_do.txt','w+')
    print_records_report = ''
    for record in records:
        print_records_report += "Study Code: "+str(record[0])+"\n"+str(record[1])

    to_do_file.write(print_records_report)
    to_do_file.close()
    
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + "\\to_do.txt"
    os.startfile(file_path)

    conn.commit()
    conn.close()

"""function to generate a handover report with data in DB in csv and open that file"""
def handover_sls_report():
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()
    conn = sqlite3.connect('studies.db')
    c = conn.cursor()

    #select all data from studies
    c.execute("SELECT * FROM studies")
    records = c.fetchall()
    #select only the column names
    c.execute("SELECT * from studies")
    column_name = [row[0] for row in c.description]
    print_records_report = ''
    #create and open the csv file and write it
    handover_file = open('handover.csv','w+')

    #add the column names in the first row in the csv file
    for column in column_name:
        handover_file.write(column + ',')

    handover_file.write('\n')
    #add all the data in the csv file
    for record in records:
            print_records_report += str(record) + "\n"

    handover_file.write(print_records_report)
    handover_file.close()

    """replace undesired elements from the csv"""
    handover_file_read = open('handover.csv', "r")
    text = ''.join([i for i in handover_file_read]).replace("(","")\
        .replace("\\n",'\\')\
        .replace(")","")
    handover_file_write=open('handover.csv', "w")
    handover_file_write.writelines(text)
    handover_file_write.close()



    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '\handover.csv'
    os.startfile(file_path)
    #widgets

    # close_report_btn = Button(handover,text="Close",command=handover.destroy, padx=10, pady=10)
    # query_label_report = Label(handover, text=print_records_report,bg="#add8e6")

    # #grid
    # close_report_btn.grid(row=0,column=0,columnspan=2,padx=5,pady=5,ipadx=50)
    # query_label_report.grid(row=2, column=0, columnspan=2,rowspan=30)



"""Button to add a new study, will open the frames function from checklist module"""
add_study_btn = Button(root, text="Add new study", command=frames, padx=10, pady=5)
"""Button to show the studies in the DB, by OID and Study code"""
show_studies_btn = Button(root, text="Show studies",command=show,padx=10, pady=5)
"""Button to open the checklist with the data from the DB, based on the record added in the search box"""
update_study_btn = Button(root, text="Update study",command=editor,padx=10, pady=5)
"""Button to delete the selected study from the DB"""
delete_study_btn = Button(root, text="Delete study", command=delete,padx=10,pady=5)
"""Button for an TO DO report"""
to_do_report_btn = Button(root,text="[TO DO]Report", command=to_do_report,padx=10,pady=5)
"""Button for Handover report"""
handover_report_btn = Button(root,text="Handover Report", command=handover_sls_report,padx=10,pady=5)

#Search label that will search on the database for the study code.
search_label = Label(root, text="Study ID",bg="#add8e6")
"""Box used to update the study, search by the OID"""
search_box = Entry(root,width=32)

#Grid
add_study_btn.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
search_label.grid(row=1,column=0)
search_box.grid(row=2,column=0, padx=10,pady=(0,10))
show_studies_btn.grid(row=0,column=3,columnspan=2,padx=10,pady=5,ipadx=50)
update_study_btn.grid(row=4,column=0,columnspan=2,padx=10,pady=5,ipadx=50)
delete_study_btn.grid(row=5,column=0,columnspan=2,padx=10,pady=5,ipadx=52)
to_do_report_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=5,ipadx=45)
handover_report_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=5,ipadx=40)


root.mainloop()