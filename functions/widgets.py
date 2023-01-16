import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
# Defining a function for creating labels (text)
def text_label (window,text,x_axis,y_axis):
    lbl=tk.Label(window,text=text)
    lbl.place(x=x_axis,y=y_axis)
    return lbl

#Defining a function for creating user entries
def text_box(window,width,x_axis,y_axis):
    txtbox=tk.Entry(window,width=width)
    txtbox.place(x=x_axis,y=y_axis)
    return txtbox

#Defining a function for creating a Button
def button(window,text,x_axis,y_axis, command=1,activebackground='pink',activeforeground='blue'):
    btn=tk.Button(window,text=text,activebackground=activebackground,activeforeground=activeforeground,command=command)
    btn.place(x=x_axis,y=y_axis)
    return btn

#Defining a function for creating a dropdown menu
def drop_down (window,options, x_axis, y_axis):
    variable=tk.StringVar(window)
    variable.set(options[0])
    menu=tk.OptionMenu(window,variable,*options)
    menu.place(x=x_axis,y=y_axis)
    return menu

#Defining a function to create Date Entry 
def date_entry(window,x_axis,y_axis): 
    cal = DateEntry(window, width= 16,date_pattern="dd-mm-y", background= "blue", foreground= "white",bd=2)
    cal.place(x=x_axis,y=y_axis)
    return cal

#Defining a function to create a combox drop down
def combo_box(window,values,width,x_axis,y_axis):
    combo=ttk.Combobox(window,width=width,value=values,state='disabled')
    combo.place(x=x_axis,y=y_axis)
    combo.set(values[0])
    return combo

#Defining a function to clear Widgets in a frame
def clear_widget(frame1):
    for widget in frame1.winfo_children():
        widget.destroy()

