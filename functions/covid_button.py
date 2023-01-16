import tkinter as tk 
from tkinter import ttk
import sys
from widgets import button, text_label,combo_box,date_entry,clear_widget
from covid.dataframe import submit_button
from helpers.area_list import areas
import datetime
from tkcalendar import Calendar,DateEntry

                
def covid(covid_frame,stopnS_frame):
    clear_widget(covid_frame)
    clear_widget(stopnS_frame)
    stopnS_frame.forget()
    covid_frame.pack(fill='both', expand=1)
    text_label(covid_frame,'Select Data to Visualize : ',50,110) 

    onedate_frame=tk.Frame(covid_frame)
    twodate_frame=tk.Frame(covid_frame)

    plots=[ 'Total cases per day over a given period',
            'Total cases per month over a given period',
            'Total cases on a given day',
            'Areas with highest cases on a given day',
            'Comparison of cases in two areas per day'
    ]

    two_dates=['Total cases per day over a given period',
            'Total cases per month over a given period'
            ]

    one_date=['Total cases on a given day',
            'Areas with highest cases on a given day','Comparison of cases in two areas per day']
    #Defining a function for the selected option from the combobox
    two_areas=['Comparison of cases in two areas per day',
               'comparison of cases in two areas over a given period']

    
    
    def selected(event):
        if combo.get() in two_dates:
            onedate_frame.pack_forget()
            twodate_frame.pack(fill='both',expand=1)
            

            #Creating Labels
            text_label(twodate_frame,'Start Date : ',50,180)
            text_label(twodate_frame,'End Date : ',320,180)
            text_label(covid_frame,'Select Data to Visualize : ',50,110) 
 

            #creating a calendar
            start_date = date_entry(twodate_frame,120,180)
            end_date = date_entry(twodate_frame,385,180)

                
            #Creating Button
            button(twodate_frame,'SUBMIT',550,175, command=lambda: submit_button(start_date.get_date(),end_date.get_date()))
            

        elif combo.get() in one_date:
            twodate_frame.forget()
            onedate_frame.pack(fill='both',expand=1) 
            
            clear_widget(onedate_frame)
            
            areas_frame=tk.Frame(onedate_frame)
            areas_frame.pack(fill='both',expand=1)
           
            text_label(covid_frame,'Select Data to Visualize : ',50,110) 
            text_label(onedate_frame,'Select Date : ',50,180)
            date_entry( onedate_frame,120,180)
            
            
            if combo.get() in two_areas:
                clear_widget(onedate_frame)
                print (areas)
                text_label(onedate_frame,'Area 1 : ',50,140)
                area1_combo=ttk.Combobox(onedate_frame,width=34,state="readonly",value=areas)
                area1_combo.place(x=100,y=140)   
                
                text_label(onedate_frame,'Area 2 : ',340,140)
                area2_combo=ttk.Combobox(onedate_frame,width=34,state="readonly",value=areas)
                area2_combo.place(x=385,y=140) 
                
                text_label(onedate_frame,'Select Date : ',50,180)
                date_entry(onedate_frame,120,180)
            
                
            
            
            
            
            #Creating Button
            button(onedate_frame,'SUBMIT',550,175) 
            
            
#Creating a combobox list
    combo=ttk.Combobox(covid_frame,width=40,state="readonly",value=plots)
    combo.place(x=190,y=110)
    combo.set('Select')
    combo.bind('<<ComboboxSelected>>',selected)       #Binding a function to a selected option from the combolist 
