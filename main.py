from tkinter import *
import checklist

root = Tk()
root.title("SLS Checklist")


#Main frame Widget
main_frame = LabelFrame(root, padx=30,pady=30)
main_frame.pack(padx=20,pady=20)

#function to open a new window for checklist
#def add_study():
   #checklist.checklist()

add_study = Button(main_frame, text="Add new study", padx =10,
    pady=10,command=add_study)
check_studies = Button(main_frame, text="Check studies",padx=10,
    pady=10,)

#main frame Grid
add_study.grid(row=0,column=0, padx=10, pady=10)
check_studies.grid(row=0,column=1, padx=10, pady=10)

#Study Frame Widget

study_frame = LabelFrame(root, text="Studies",padx=20,pady=20)
study_frame.pack()





root.mainloop()

