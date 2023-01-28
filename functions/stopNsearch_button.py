import tkinter as tk 
from widgets import button, text_label,combo_box,date_entry,clear_widget
from stop_and_search.functions import search_by_gender, search_by_officer_defined_ethnicity, search_by_legislation, search_by_type, search_outcome, search_by_age_range_that_resulted_in_arrest
from stop_and_search.api_request import fetch_list_of_police_forces
from  datetime import date

def stop_n_search(covid_frame,stopnS_frame):
        clear_widget(covid_frame)
        clear_widget(stopnS_frame)
        covid_frame.forget()
        stopnS_frame.pack(fill='both', expand=1)
    
        text_label(stopnS_frame,'Select option to Visualize : ',50,110) 
        frame=tk.Frame(stopnS_frame)
        options=[ 
                'Stop and search cases gender',
                'Stop and search result by age range that resulted in arrest',
                'Stop and search cases by officer defined ethnicity',
                'Stop and search cases by legislation',
                'Type of stop and search cases',
                'Outcome of stop and search cases',
        ]
    
        def selected(e):
                #Creating Labels
                frame.pack(fill='both',expand=1)
                text_label(frame,'Select date : ',50,160)
                text_label(frame,'Select option to Visualize : ',50,110) 

                #creating a calendar
                date_month = date_entry(frame,130,160, min_date=date(2020,1,1), max_date=date(2022,12,31))
                text_label(frame,'Select police force : ',50,205)
                police_forces = list(fetch_list_of_police_forces().keys())
                police_force_combo= combo_box(window=frame,values=police_forces,width=30,x_axis=180,y_axis=205)
                police_force_combo.set(police_forces[1])

                button(frame,'SUBMIT',130,250, command=lambda: check_case_option(date_month.get(),police_force_combo.get()))

                def check_case_option(date, police_force):
                        if combo.get() == "Stop and search cases gender":
                                return search_by_gender(date, police_force)
                        elif combo.get() == "Stop and search result by age range that resulted in arrest":
                                return search_by_age_range_that_resulted_in_arrest(date, police_force)
                        elif combo.get() == "Stop and search cases by officer defined ethnicity":
                                return search_by_officer_defined_ethnicity(date, police_force)
                        elif combo.get() == "Stop and search cases by legislation":
                                return search_by_legislation(date, police_force)
                        elif combo.get() == "Type of stop and search cases":
                                return search_by_type(date, police_force)
                        elif combo.get() == "Outcome of stop and search cases":
                                return search_outcome(date, police_force)

        #Creating a combobox list
        combo = combo_box(window=stopnS_frame,values=options,width=40,x_axis=220,y_axis=110)
        combo.set('Select')
        combo.bind('<<ComboboxSelected>>', selected)       #Binding a function to a selected option from the combolist 

        text_label(covid_frame,'Select Data to Visualize : ',50,110)  