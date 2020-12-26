from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from checklist import frames, frames_updates


root = Tk()
root.title("SLS Checklist")
root.iconbitmap('images/fire_eye_alien.ico')
root.configure(bg="#add8e6")
root.geometry('500x300')


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
    query_label.grid(row=2, column=3, columnspan=2,rowspan=30)

    conn.commit()
    conn.close()

def editor():
    frames_updates()
    conn = sqlite3.connect('studies.db')
    c =  conn.cursor()
    record_id = select_box.get()
    c.execute("SELECT * FROM adresses WHERE oid = " + record_id)
    records=c.fetchall()

    for records in records:
        sponsor_box.insert(0, record[0])
        study_code_box.nsert(0, record[1])
        language_number_box.nsert(0, record[2])
        pm_name_box.nsert(0, record[3])
        pds_name_box.nsert(0, record[4])
        device_type_box.insert(0, record[5])
        internal_kom_var.insert(0, record[6])
        check_wf_var.insert(0, record[7])
        sls_task_var.insert(0, record[8])
        draft_lp_var.insert(0, record[9])
        loca_kom_var.insert(0, record[10])
        check_msr_var.insert(0, record[11])
        check_mqrg_var.insert(0, record[12])
        check_ldc_var.insert(0, record[13])
        check_paper_source_var.insert(0, record[14])
        check_translation_service_var.insert(0, record[15])
        check_tft_var.insert(0, record[16])
        check_irb_var.insert(0, record[17])
        check_quote_var.insert(0, record[18])
        check_po_var.insert(0, record[19])
        add_quote_po_oct_var.insert(0, record[20])
        loca_plan_var.insert(0, record[21])
        access_ts_tm_var.insert(0, record[22])
        assign_ls_wf_var.insert(0, record[23])
        access_platform_var.insert(0, record[24])
        handover_ls_var.insert(0, record[25])
        text.insert(0, record[26])
        to_do_textbox.insert(0, record[27])
    conn.commit()
    conn.close()
"""Button to add a new study, will open the frames function from checklist module"""
add_study = Button(root, text="Add new study", command=frames, padx=10, pady=5)
show_studies = Button(root, text="Show studies",command=show,padx=10, pady=5)
update_study = Button(root, text="Update study",command=editor,padx=10, pady=5)

#Search label that will search on the database for the study code.
search_label = Label(root, text="Study ID",bg="#add8e6")
search_box = Entry(root,width=35)

#Grid
add_study.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
search_label.grid(row=1,column=0)
search_box.grid(row=2,column=0, padx=10,pady=(0,10))
show_studies.grid(row=0,column=3,columnspan=2,padx=10,pady=5,ipadx=50)
update_study.grid(row=4,column=0,columnspan=2,padx=10,pady=5,ipadx=50)


root.mainloop()

