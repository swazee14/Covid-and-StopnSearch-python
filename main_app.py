import tkinter as tk 
from tkcalendar import Calendar,DateEntry
from functions.widgets import button, text_label
from functions.covid_button import covid
from functions.stopNsearch_button import stop_n_search

def index():
    #Creating the GUI window
    root=tk.Tk()
    root.geometry('700x600')
    root.title('Jidechukwu Ezeh - B1484164')

    # Creating Frames for Covid and Stop and Search
    covid_frame=tk.Frame(root)
    stopnS_frame=tk.Frame(root)

    #Creating  labels
    text_label(root,'SOFTWARE FOR DIGITAL INNOVATION - Element 2 ',20,20)
    text_label(root,'DATA SET : ',50,65)

    #Creating Buttons
    button(root,'COVID',120,60,command=lambda:covid(covid_frame,stopnS_frame))  
    button(root,'STOP AND SEARCH',220,60,command=lambda:stop_n_search(stopnS_frame,covid_frame))
    return root

if __name__ == "__main__":
    index().mainloop()