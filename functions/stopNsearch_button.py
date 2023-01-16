import tkinter as tk 
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from widgets import button, text_label,combo_box,date_entry,clear_widget
def stop_n_search(stopnS_frame,covid_frame):
    clear_widget(covid_frame)
    clear_widget(stopnS_frame)
    covid_frame.forget()
    stopnS_frame.pack(fill='both', expand=1)


    plots=[ 'A',
            'B',
            'C',
            'D',
            'E'
    ]
  
    #Creating a combobox list
    combo=ttk.Combobox(stopnS_frame,width=40,value=plots)
    combo.place(x=190,y=110)
    combo.set(plots[0])


     #Creating  labels
    text_label(covid_frame,'Select Data to Visualize : ',50,110)  
    