import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import sys
import tkinter as tk 
from tkinter import messagebox


# Importing the CSV file 
covid_df=pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

# Creating a new dataframe with only relevant columns
covid_df=covid_df[['areaType','areaCode','areaName','date','newCasesBySpecimenDate-0_59','newCasesBySpecimenDate-60+']]

# Deleting all rows with empty columns
covid_df1=covid_df.dropna(inplace=False)

#creating a new column which contains the total number of new cases by specimen date
covid_df1["newCasesBySpecimenDate-Total"] = (covid_df1["newCasesBySpecimenDate-0_59"] + covid_df1["newCasesBySpecimenDate-60+"])

#Creating new columns to show the percentage change in new cases by specimen date
covid_df1['PercentageChange-cases-0_59']=covid_df1["newCasesBySpecimenDate-0_59"].pct_change() * 100
covid_df1['PercentageChange-cases-60+']=covid_df1["newCasesBySpecimenDate-60+"].pct_change() * 100
covid_df1['PercentageChange-cases_Total']=covid_df1["newCasesBySpecimenDate-Total"].pct_change() * 100

# Replacing infs with NaN and filling NaNs  with 0
covid_df1.replace([np.inf, -np.inf], np.nan, inplace=True)
covid_df1.fillna(0, inplace=True)

def submit_button(start,end):
    print (end==start)
    if  end<=start:
        tk.messagebox.showinfo('Invalid Date Range', 'Start date must be earlier than end date')
        
    else:
        covid_df.plot(kind='scatter', x='areaName', y='newCasesBySpecimenDate-60+')
        plt.show()


