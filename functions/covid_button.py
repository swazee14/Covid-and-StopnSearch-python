import tkinter as tk 
from widgets import button, text_label,combo_box,date_entry,clear_widget
from covid_functions import cases_per_month_over_a_period, compare_two_areas_per_day, cases_on_a_given_day, areas_with_highest_cases_on_a_given_day, cases_per_day_over_a_period
from helpers.area_list import areas
                
def covid(covid_frame,stopnS_frame):
    clear_widget(covid_frame)
    clear_widget(stopnS_frame)
    stopnS_frame.forget()
    covid_frame.pack(fill='both', expand=1)
    text_label(covid_frame,'Select Data to Visualize : ',50,110) 

    onedate_frame=tk.Frame(covid_frame)
    twodate_frame=tk.Frame(covid_frame)

    plots=[ 
        'Total cases per day over a given period',
        'Total cases per month over a given period',
        'Total cases on a given day',
        'Areas with highest cases on a given day',
            'Comparison of cases in two areas per day'
    ]
    
    def selected(event):
        if combo.get() == "Total cases per day over a given period":
            onedate_frame.pack_forget()
            twodate_frame.pack(fill='both',expand=1)
            
            #Creating Labels
            text_label(twodate_frame,'Start Date : ',50,180)
            text_label(twodate_frame,'End Date : ',310,180)
            text_label(covid_frame,'Select Data to Visualize : ',50,110) 
 
            #creating a calendar
            start_date = date_entry(twodate_frame,130,180)
            end_date = date_entry(twodate_frame,380,180, month=10, day=20)
 
            #Creating Button
            button(twodate_frame,'SUBMIT',570,175, command=lambda: cases_per_day_over_a_period(start_date.get(),end_date.get()))
            
        elif combo.get() == "Total cases per month over a given period":
            onedate_frame.pack_forget()
            twodate_frame.pack(fill='both',expand=1)
            
            #Creating Labels
            text_label(twodate_frame,'Start Date : ',50,180)
            text_label(twodate_frame,'End Date : ',310,180)
            text_label(covid_frame,'Select Data to Visualize : ',50,110) 
 
            #creating a calendar
            start_date = date_entry(twodate_frame,130,180)
            end_date = date_entry(twodate_frame,380,180, month=10, day=20)
 
            #Creating Button
            button(twodate_frame,'SUBMIT',570,175, command=lambda: cases_per_month_over_a_period(start_date.get(),end_date.get()))
            
        elif combo.get() == "Total cases on a given day":
            twodate_frame.pack_forget()
            onedate_frame.pack(fill='both',expand=1) 
            
            areas_frame=tk.Frame(onedate_frame)
            areas_frame.pack(fill='both',expand=1)
           
            text_label(onedate_frame,'Select Data to Visualize : ',50,110) 
            text_label(onedate_frame,'Select Date : ',50,180)
            date = date_entry( onedate_frame,150,180)
            
            button(onedate_frame,'SUBMIT',150,280, command=lambda: cases_on_a_given_day(date.get())) 
            
        elif combo.get() == "Areas with highest cases on a given day":
            twodate_frame.pack_forget()
            onedate_frame.pack(fill='both',expand=1) 
            
            areas_frame=tk.Frame(onedate_frame)
            areas_frame.pack(fill='both',expand=1)
           
            text_label(onedate_frame,'Select Data to Visualize : ',50,110) 
            text_label(onedate_frame,'Select Date : ',50,180)
            date = date_entry( onedate_frame,150,180)
            
            button(onedate_frame,'SUBMIT',150,280, command=lambda: areas_with_highest_cases_on_a_given_day(date.get())) 
        
        elif combo.get() == "Comparison of cases in two areas per day":
            twodate_frame.pack_forget()
            clear_widget(onedate_frame)
            onedate_frame.pack(fill='both',expand=1) 
            
            text_label(onedate_frame,'Area 1 : ',50,150)
            area1_combo= combo_box(window=onedate_frame,values=areas,width=34,x_axis=100,y_axis=150)
            area1_combo.set(areas[18])
            
            text_label(onedate_frame,'Area 2 : ',50,190)
            area2_combo= combo_box(window=onedate_frame,values=areas,width=34,x_axis=100,y_axis=190)
            area2_combo.set(areas[33])
            
            text_label(onedate_frame,'Select Date : ',50,230)
            date = date_entry(onedate_frame,140,230)
    
            #Creating Button
            button(onedate_frame,'SUBMIT',150,280, command=lambda: compare_two_areas_per_day(area1_combo.get(), area2_combo.get(), date.get())) 

#Creating a combobox list
    combo = combo_box(window=covid_frame,values=plots,width=40,x_axis=220,y_axis=110)
    combo.set('Select')
    combo.bind('<<ComboboxSelected>>',selected)       #Binding a function to a selected option from the combolist 
