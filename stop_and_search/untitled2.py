import tkinter as tk
from tkcalendar import DateEntry, Calendar
root2=tk.Tk()
root2.geometry('500x500')
cal = DateEntry(root2, width= 16, date_pattern="dd-mm-y", background= "blue", foreground= "white",bd=2)
cal.place(x=120,y=180)
bt1=tk.Button(root2,text='Run',command=lambda:stuff())
bt1.place(x=120,y=90)

  
def stuff(): 
    def print_sel(e):
        print(cal.get_date())
    cal.bind("<<DateEntrySelected>>", print_sel)

word=cal.get_date()


tk.mainloop()
